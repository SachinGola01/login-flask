from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
# jhryufg34r


templates = Jinja2Templates(directory="templates")



@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )



@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):

    
    correct_password = "1234"

    if "@" in email  and password == correct_password and username:
        return templates.TemplateResponse(
            "dashboard.html",
            {
                "request": request,
                "username": username
            }
        )
    else:
        return templates.TemplateResponse(
            "login.html",
            {
                "request": request,
                "error": "Invalid username or password"
            }
        )


if __name__ == "__main__":
    uvicorn.run("app1:app", host="127.0.0.1", port=8002, reload=True)
