from fastapi import FastAPI, HTTPException, Depends
from tortoise.contrib.fastapi import register_tortoise
from app import config, crud
from app.schemas import UserCreate , UserUpdate , UserOut, UserFilterDTO, RoleOut, RoleCreate , UserRoleMap

app = FastAPI()

@app.post("/user", response_model=UserOut)
async def create_user(user: UserCreate):
    return await crud.create_user(user) 

@app.get("/user/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    user = await crud.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/filter/users", response_model=list[UserOut])
async def get_users(params:UserFilterDTO = Depends()):
    print(params)
    users = await crud.get_all_users(params)
    if users is None:
        raise HTTPException(status_code=404, detail="No Users Exist")
    return users


@app.put("/update/user/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user_data: UserUpdate):
    user = await crud.update_user(user_id, user_data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.patch("/update/user/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user_data: UserUpdate):
    data_dict = user_data.dict(exclude_unset=True)
    if len(data_dict) != 1:
        raise HTTPException(status_code=402, detail="Only one field can be updated at a time")
    user = await crud.update_user(user_id, user_data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/delete/user/{user_id}")
async def delete_user(user_id: int):
    success = await crud.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted","id":user_id}

@app.post("/create/role", response_model=RoleOut)
async def create_role(role:RoleCreate):
    return await crud.create_role(role)

@app.get("/filter/role", response_model=list[RoleOut])
async def get_role():
    role = await crud.get_all_role()
    if role is None:
        raise HTTPException(status_code=404, detail="No Role Exist")
    return role

@app.put("/user-role-map", response_model=UserOut)
async def map_role_user(data:UserRoleMap):
    return await crud.user_role_map(data)

register_tortoise(
    app,
    config=config.TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)