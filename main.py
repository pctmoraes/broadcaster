from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.view.connection_view import route

app = FastAPI()
app.include_router(route)

@app.get("/broadcaster")
async def get():
    return HTMLResponse(open("app/templates/chat.html").read())
