import os

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(title="Nexa Panel")

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET", "nexa-secret-change-me"),
)

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")


LOGIN_PAGE = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXA - Login</title>
    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            min-height: 100vh;
            background: #080b12;
            color: white;
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

        h1 { text-align: center; margin: 0; }

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
        <input type="text" name="username" placeholder="نام کاربری" required>
        <input type="password" name="password" placeholder="رمز عبور" required>
        <button type="submit">ورود</button>
    </form>
</div>
</body>
</html>
"""


DASHBOARD = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexa Panel</title>
    <style>
        body {
            margin: 0;
            background: #080b12;
            color: white;
            font-family: Arial, sans-serif;
        }

        .box {
            max-width: 900px;
            margin: 80px auto;
            padding: 30px;
            background: #0d111a;
            border: 1px solid #1d2430;
            border-radius: 18px;
        }

        h1 { margin-top: 0; }

        .success {
            color: #48d597;
        }

        a {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 18px;
            background: #5b5bf7;
            color: white;
            text-decoration: none;
            border-radius: 10px;
        }
    </style>
</head>

<body>
<div class="box">
    <h1>NEXA Panel 🚀</h1>
    <p class="success">ورود با موفقیت انجام شد.</p>
    <p>خوش آمدید، مدیر سیستم.</p>

    <a href="/logout">خروج</a>
</div>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    if request.session.get("logged_in"):
        return HTMLResponse(DASHBOARD)

    return HTMLResponse(LOGIN_PAGE)


@app.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        request.session["logged_in"] = True
        return RedirectResponse("/", status_code=303)

    return HTMLResponse(
        """
        <div style="text-align:center;margin-top:100px;font-family:Arial">
            <h3>نام کاربری یا رمز عبور اشتباه است.</h3>
            <a href="/">بازگشت</a>
        </div>
        """,
        status_code=401,
    )


@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)
