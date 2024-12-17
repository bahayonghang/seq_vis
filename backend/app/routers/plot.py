from fastapi import APIRouter, Form
from fastapi.responses import FileResponse
from pathlib import Path
from app.utils.plotter import plot_train_results, plot_test_results

router = APIRouter()

@router.post("/plot/train")
async def plot_train(folder_path: str = Form(...)):
    folder = Path(folder_path)
    if not folder.exists():
        return {"error": "Folder not found"}
    try:
        plot_file = plot_train_results(folder)
        return FileResponse(plot_file, media_type="image/png")
    except Exception as e:
        return {"error": str(e)}

@router.post("/plot/test")
async def plot_test(folder_path: str = Form(...)):
    folder = Path(folder_path)
    if not folder.exists():
        return {"error": "Folder not found"}
    try:
        plot_file = plot_test_results(folder)
        return FileResponse(plot_file, media_type="image/png")
    except Exception as e:
        return {"error": str(e)}
