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


# 全てのアイテムを取得
def find_all():
    return items


# IDでアイテムを取得
def find_by_id(id: int):
    for item in items:
        if item.id == id:
            return item
    return None


# 大文字の英語をキーワードで検索
def find_by_name(name: str):
    filtered_items = []

    for item in items:
        if name in item.name:
            filtered_items.append(item)
    return filtered_items


# アイテムを追加
def create(item_create):
    new_item = Item(
        len(items) + 1,  # len(items)でアイテムの数を取得し、+1で新しいアイテムのIDを設定
        item_create.get("name"),
        item_create.get("price"),
        item_create.get("description"),
        ItemStatus.ON_SALE
    )
    items.append(new_item)
    return new_item


def update(id: int, item_update):
    for item in items:
        if item.id == id:
            item.name = item_update.get("name")
            item.price = item_update.get("price")
            item.description = item_update.get("description")
            return item
    return None


def delete(id: int):
    for i in range(len(items)):
        if items[i].id == id:
            delete_item = items.pop(i)
            return delete_item
    return None
