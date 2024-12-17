from fastapi import FastAPI
from app.routers import plot

app = FastAPI()

# 注册路由
app.include_router(plot.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Result Plotter API!"}
