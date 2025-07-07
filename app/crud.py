from app.models import User, Role
from fastapi import HTTPException

async def create_user(data):
    user = await User.create(**data.dict())
    await user.fetch_related("role")  # ensure role is included, even if None
    return user

async def get_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if user:
        await user.fetch_related("role")
    return user

async def get_all_users(params):
   
    filter_dict = get_filter_object(params)
    users = await User.filter(**filter_dict).all()
    return users

def get_filter_object(params):
    filter_items = {
        "name_start_with": "name__istartswith",
        "name": "name__icontains",
        "name_end_with": "name__iendswith",
        "age": "age",
        "age_gt": "age__gt",
        "age_gte": "age__gte",
        "age_lt": "age__lt",
        "age_lte": "age__lte",
        "vill": "vill__icontains",
        "state": "state__icontains",
        "pin": "pin"
    }
    filter_dict = {}
    
    for key, value in filter_items.items():
        result = getattr(params, key)
        if result is not None:
            filter_dict[value] = result
    return filter_dict

async def update_user(user_id: int, data):
    user = await User.get_or_none(id=user_id)
    if user:
        data_dict = data.dict(exclude_unset=True)
        for key, value in data_dict.items():
            setattr(user, key, value)
        await user.save()
    return user

async def delete_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if user:
        await user.delete()
        return True
    return False

async def create_role(role):
    return await Role.create(**role.dict())

async def get_all_role():
    return await Role.all()

async def user_role_map(data):
    user = await User.get_or_none(id=data.user_id)
    role = await Role.get_or_none(id=data.role_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    user.role = role
    await user.save()
    await user.fetch_related("role")
    return user