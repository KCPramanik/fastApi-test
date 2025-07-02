from app.models import User
from app.schemas import UserFilterDTO

async def create_user(data):
     return await User.create(**data.dict())

async def get_user(user_id: int):
    return await User.get_or_none(id=user_id)

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

