# vidGPT

Прототип оффлайн‑приложения, вдохновлённого YouTube, которое генерирует видео с помощью ИИ.

## Запуск

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустите backend:
   ```bash
   uvicorn backend.app:app --reload
   ```
3. Откройте `frontend/index.html` в браузере.

## Тесты

```bash
pytest
```
