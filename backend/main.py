from ast import main
from fastapi import FastAPI
from app.routers import plot

app = FastAPI()

# 注册路由
app.include_router(plot.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Result Plotter API!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    