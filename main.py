from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Nexa Panel")


@app.get("/", response_class=HTMLResponse)
def login():

    return """
<!DOCTYPE html>
<html lang="fa" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexa Panel - Login</title>

    <style>
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
            width: 350px;
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
            font-size: 13px;
        }

        input {
            width: 100%;
            box-sizing: border-box;
            margin-top: 12px;
            padding: 13px;
            border-radius: 10px;
            border: 1px solid #1d2430;
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

    <form>
        <input type="text" placeholder="نام کاربری">

        <input type="password" placeholder="رمز عبور">

        <button type="submit">
            ورود
        </button>
    </form>

</div>

</body>
</html>
"""
