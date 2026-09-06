from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Nexa Panel")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nexa Panel</title>
    </head>
    <body>
        <h1>Nexa Panel</h1>
        <p>پنل با موفقیت اجرا شد.</p>
    </body>
    </html>
    """
