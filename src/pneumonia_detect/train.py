import logging

from omegaconf import DictConfig

log = logging.getLogger(__name__)


def train_model(cfg: DictConfig):
    log.info("=== ЗАПУСК ОБУЧЕНИЯ (MOCK) ===")
    log.info(f"Используем модель: {cfg.model.name}")
    log.info(f"Epochs={cfg.training.num_train_epochs}, LR={cfg.model.learning_rate}")

    log.info("Скачивание данных проверено. Конфиг загружен корректно.")
    log.info("=== КОНЕЦ ОБУЧЕНИЯ ===")
