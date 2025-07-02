from typing import Annotated
from fastapi import Path, APIRouter


'''
Здесь мы создавем router для того, чтобы связать его с основной view(main.py). Аттрибут prefix нужен, чтобы 
каждый раз не писать в get('/items'), мы это явно указываем в роутере для всех get и post запросов связанных с items.
tags - нужен, чтобы в интерактивной документации, все url адреса не находились в одной группе, а были разделены, 
так мы все url адресам items, отобрали в отдельную группу.
'''
router = APIRouter(prefix="/items", tags=["Items"])


@router.get('/')
def list_items():
    return [
        "Items_1",
        "Items_2"
    ]


@router.get('/latest/')
def get_latest_item():
    return {"item": {"id": '0', "name": "latest"}}


@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
       "Item": {
           "id": item_id
        },
    }
    
