import uvicorn
from fastapi import FastAPI, Body
from cruds import item as item_crud

app = FastAPI()


@app.get("/items")
async def find_all():
    return item_crud.find_all()


@app.get("/items/{id}")
async def find_by_id(id: int):
    return item_crud.find_by_id(id)


# 同じパスだと名前の衝突が起きるので、パスを変更
@app.get("/items/")
async def find_by_name(name: str):
    return item_crud.find_by_name(name)


# HTTP POST配列にデータを追加する。リクエストボディで送信される。
@app.post("/items")
async def create(item_create=Body()):
    return item_crud.create(item_create)


# HTTP PUTでデータを更新する。リクエストボディで送信される。
@app.put("/items/{id}")
async def update(id: int, item_update=Body()):
    return item_crud.update(id, item_update)


# HTTP DELETEでデータを削除する。
@app.delete("/items/{id}")
async def delete(id: int):
    return item_crud.delete(id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
