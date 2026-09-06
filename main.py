import os

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Nexa Panel")

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET", "change-this-secret"),
)

app.mount("/static", StaticFiles(directory="static"), name="static")


ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")


@app.get("/", response_class=HTMLResponse)
def home():

    return """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexa Panel</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: #080b12;
            color: #fff;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .login-box {
            width: 360px;
            background: #0d111a;
            border: 1px solid #1d2430;
            border-radius: 18px;
            padding: 30px;
        }

        h1 {
            margin: 0;
            text-align: center;
        }

        p {
            text-align: center;
            color: #697386;
        }

        input {
            width: 100%;
            margin-top: 12px;
            padding: 13px;
            border: 1px solid #1d2430;
            border-radius: 10px;
            background: #080b12;
            color: white;
        }

        button {
            width: 100%;
            margin-top: 18px;
            padding: 13px;
            border: 0;
            border-radius: 10px;
            background: #5b5bf7;
            color: white;
            cursor: pointer;
        }
    </style>
</head>

<body>

<div class="login-box">

    <h1>NEXA</h1>

    <p>ورود به پنل مدیریت</p>

    <form method="post" action="/login">
        <input
            type="text"
            name="username"
            placeholder="نام کاربری"
            required
        >

        <input
            type="password"
            name="password"
            placeholder="رمز عبور"
            required
        >

        <button type="submit">
            ورود
        </button>
    </form>

</div>

</body>
</html>
"""


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        response = RedirectResponse("/", status_code=303)
        response.set_cookie("nexa_logged_in", "1", httponly=True)
        return response

    return HTMLResponse(
        "<h3 style='text-align:center;margin-top:100px'>نام کاربری یا رمز عبور اشتباه است.</h3>",
        status_code=401,
    )
