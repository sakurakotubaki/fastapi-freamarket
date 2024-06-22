from enum import Enum
from typing import Optional


# CRUDを行うクラス

class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"


class Item:
    def __init__(
            self,
            id: int,
            name: str,
            price: int,
            description: Optional[str],
            status: ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status


## ダミーデータ
items = [
    Item(1, "PC", 100, "description1", ItemStatus.ON_SALE),
    Item(2, "iPhone", 100000, None, ItemStatus.ON_SALE),
    Item(3, "Android", 50000, "description1", ItemStatus.ON_SALE),
]


def find_all():
    return items


def find_by_id(id: int):
    for item in items:
        if item.id == id:
            return item
    return None


def find_by_name(name: str):
    filtered_items = []

    for item in items:
        if name in item.name:
            filtered_items.append(item)
    return filtered_items
