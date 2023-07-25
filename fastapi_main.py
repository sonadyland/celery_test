from typing import Optional, Union, List, Set

from fastapi import FastAPI, Query, Cookie, Header, Body, Path, Form, File, UploadFile, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel


app = FastAPI()
data_list = [{'a': 1}, {'b': 4}, {'c': 5}]


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str = None
    # Optional[X] is equivalent to Union[X, None]
    # You can use Optional[X] as a shorthand for Union[X, None]
    type: Optional[str] = None
    description: Union[str, int, None] = None
    price: List[float] = []
    tax: float
    image: List[Union[Image, None]] = []


class Success(BaseModel):
    status: int = 1
    msg: str = '请求成功'
    data: dict


@app.get("/")
def read_root():
    return {"Hello": "World"}


# 接收路径参数与查询参数
@app.get("/items/{item_id}")
def read_item(imp: str = None,
              q: Optional[str] = None,
              item_id: int = Path(...)
              ):  # imp: bool 为必传参数, q: Optional[str] = None 为可选参数
    return {"item_id": item_id, "q": q, "imp": imp}


# 接收路径参数
@app.get("/data/{key}")
async def get_data(key: Optional[str] = Path(..., title='key')):
    for data in data_list:
        if key in data:
            return data
    return {'error': 'not found'}


# 接收body参数
@app.post("/items")
async def read_items(item: Item):
    return [{"name": item.name}, {"description": item.description}, {"price": item.price}, {"tax": item.tax}, {"type": item.type},
            {"image": item.image}]


# 接收header信息
@app.post("/header")
async def read_header(user_agent: Optional[str] = Header(None)):
    return JSONResponse(
        Success(data={'user_agent': user_agent}).dict(),
        status_code=status.HTTP_200_OK,
        headers={'sign': ''},
        # {
        #     'code': 200,
        #     'message': "Success",
        #     'data': user_agent,
        # }
    )
