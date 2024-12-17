from pathlib import Path
from industrytslib.utils.visualization.matplotlib_plotter import plot_npy_all, plot_npy_all_train

def plot_train_results(folder: Path) -> Path:
    plot_npy_all_train(folder)
    return folder / "true_pred_all_train.png"

def plot_test_results(folder: Path) -> Path:
    plot_npy_all(folder)
    return folder / "true_pred_all.png"
