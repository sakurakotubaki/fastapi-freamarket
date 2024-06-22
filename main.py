import uvicorn
from fastapi import FastAPI
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
