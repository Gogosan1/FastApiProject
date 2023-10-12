from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
# при запуске передается полная веб страница
app = FastAPI()



"""
#GET (получение информации о данных или списка объектов)
#DELETE (удаление данных)
#POST (добавление или замена данных)
#PUT (регулярное обновление данных)
#routing - маршрутизация запросов к серверу
#repositories - работа с базами данных
#services - бизнес логика приложения

#@app.get("/")
def send_main_page():
    return FileResponse("WEB_client/pages/index.html")

@app.get("/{style}.css")
def send_registration_page(style):
    return FileResponse("WEB_client/styles/{style}.css")


@app.get("/styles/{style}.css")
def send_registration_page():
    return FileResponse("WEB_client/styles/{style}.css")


@app.get("/{page}.html")
def send_registration_page():
    return FileResponse("WEB_client/pages/{page}.html")

#@app.get("/styles/{registration}.css")
#def send_registration_page():
#    return FileResponse("WEB_client/styles/{registration}.css")


#получение данных для входа
@app.get("/sign_in")
def get_data(email = Form(), password = Form()):
    return {"email": email, "password": password}
"""