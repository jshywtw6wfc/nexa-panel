from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Nexa Panel")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def dashboard():

    return """
<!DOCTYPE html>
<html lang="fa" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Nexa Panel</title>

    <link rel="stylesheet" href="/static/style.css">
</head>

<body>

<div class="container">

    <aside class="sidebar">

        <div class="logo">
            <h1>NEXA</h1>
            <span>CONTROL PANEL</span>
        </div>

        <nav class="menu">

            <button class="active">
                <span>◈ &nbsp; داشبورد</span>
            </button>

            <button>
                <span>◉ &nbsp; کاربران</span>
            </button>

            <button>
                <span>◇ &nbsp; سرویس‌ها</span>
            </button>

            <button>
                <span>▣ &nbsp; گزارش‌ها</span>
            </button>

            <button>
                <span>⚙ &nbsp; تنظیمات</span>
            </button>

        </nav>

    </aside>


    <section class="content">

        <header class="header">

            <div>
                <h2>داشبورد</h2>

                <p>
                    مدیریت و نظارت بر سیستم
                </p>
            </div>


            <div class="profile">

                <div>
                    <strong>Admin</strong>
                </div>

                <div class="avatar">
                    A
                </div>

            </div>

        </header>


        <main class="main">

            <section class="cards">

                <div class="card">

                    <div class="card-title">
                        کاربران
                    </div>

                    <div class="card-value">
                        128
                    </div>

                    <div class="card-info">
                        کاربران ثبت شده
                    </div>

                </div>


                <div class="card">

                    <div class="card-title">
                        آنلاین
                    </div>

                    <div class="card-value">
                        47
                    </div>

                    <div class="card-info">
                        اتصال فعال
                    </div>

                </div>


                <div class="card">

                    <div class="card-title">
                        مصرف امروز
                    </div>

                    <div class="card-value">
                        184 GB
                    </div>

                    <div class="card-info">
                        ترافیک مصرف شده
                    </div>

                </div>


                <div class="card">

                    <div class="card-title">
                        وضعیت سیستم
                    </div>

                    <div class="card-value">
                        Online
                    </div>

                    <div class="card-info">
                        همه سرویس‌ها فعال هستند
                    </div>

                </div>

            </section>


            <section class="panel">

                <div class="panel-header">

                    <div>
                        <h3>
                            کاربران اخیر
                        </h3>

                        <span>
                            آخرین کاربران سیستم
                        </span>
                    </div>

                </div>


                <table>

                    <thead>

                        <tr>
                            <th>کاربر</th>
                            <th>وضعیت</th>
                            <th>مصرف</th>
                            <th>انقضا</th>
                        </tr>

                    </thead>


                    <tbody>

                        <tr>

                            <td>
                                Ali
                            </td>

                            <td>
                                <span class="status online">
                                    فعال
                                </span>
                            </td>

                            <td>
                                42.8 GB
                            </td>

                            <td>
                                12 روز
                            </td>

                        </tr>


                        <tr>

                            <td>
                                Reza
                            </td>

                            <td>
                                <span class="status online">
                                    فعال
                                </span>
                            </td>

                            <td>
                                18.2 GB
                            </td>

                            <td>
                                24 روز
                            </td>

                        </tr>


                        <tr>

                            <td>
                                Sara
                            </td>

                            <td>
                                <span class="status offline">
                                    منقضی
                                </span>
                            </td>

                            <td>
                                91.4 GB
                            </td>

                            <td>
                                تمام شده
                            </td>

                        </tr>

                    </tbody>

                </table>

            </section>

        </main>

    </section>

</div>

</body>
</html>
"""
