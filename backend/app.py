from fastapi import FastAPI
from .ai_agents import plot_ai, consensus_ai, media_generator

app = FastAPI(title="vidGPT")


@app.get("/")
def read_root():
    """Простой проверочный эндпоинт."""
    return {"message": "vidGPT backend работает"}


@app.post("/generate")
def generate_video(data: dict):
    """Маршрут, который имитирует генерацию видео по запросу пользователя."""
    plot = plot_ai.generate_plot(data.get("история", []))
    refined = consensus_ai.refine_plot(plot)
    video_path = media_generator.generate_video(refined)
    return {"video_path": video_path}
