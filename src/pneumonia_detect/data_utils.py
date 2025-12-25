import logging
import subprocess
from pathlib import Path

log = logging.getLogger(__name__)


def download_data(dataset_path: Path) -> None:
    if dataset_path.exists() and any(dataset_path.iterdir()):
        log.info(f"Данные уже существуют в: {dataset_path}")
        return

    log.info(f"Данные не найдены в {dataset_path}. Начинаем загрузку...")

    dataset_path.parent.mkdir(parents=True, exist_ok=True)

    kaggle_dataset_name = "paultimothymooney/chest-xray-pneumonia"

    try:
        subprocess.run(
            [
                "kaggle",
                "datasets",
                "download",
                "-d",
                kaggle_dataset_name,
                "--unzip",
                "-p",
                str(dataset_path),
            ],
            check=True,
        )
        log.info("Загрузка и распаковка завершены успешно.")
    except FileNotFoundError:
        log.error(
            "Kaggle CLI не найден. Убедитесь, что 'kaggle' установлен "
            "и файл kaggle.json находится в ~/.kaggle/"
        )
        raise
    except subprocess.CalledProcessError as err:
        log.error(f"Ошибка при загрузке данных с Kaggle: {err}")
        raise


def get_dvc_file(dataset_path: Path) -> Path:
    return dataset_path.parent / (dataset_path.name + ".dvc")
