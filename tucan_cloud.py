from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Datos de tu agente
TUCAN_DATA = {
    "tucan": "TucanTucumanoChanguero vivo en la nube!",
    "changa": "/changa",
    "precio": "0.001 POL",
    "direccion": "agent1qvs9087jse6d4c2hhyKj5x2d4z1q6g9yc1cwwX2zdkjns3228xa1ta16e"
}

@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Tucán Tucumano 🦜</title>
        <style>
            body {{ font-family: sans-serif; background: #fff8e1; text-align: center; padding: 20px; }}
            .card {{ background: white; border-radius: 20px; padding: 30px; max-width: 400px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
            .tucan {{ font-size: 80px; }}
            h1 {{ color: #ff6f00; }}
            .precio {{ font-size: 24px; background: #ffecb3; padding: 10px; border-radius: 10px; margin: 15px 0; }}
            .btn {{ display: block; background: #ff6f00; color: white; padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 20px; }}
            .dir {{ font-size: 10px; word-break: break-all; color: #888; margin-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="tucan">🦜</div>
            <h1>Tucán Tucumano</h1>
            <p><b>{TUCAN_DATA['tucan']}</b></p>
            <p>El changuero más piola de Tucumán, ahora en la nube ☁️</p>
            <div class="precio">💰 Precio changa: {TUCAN_DATA['precio']}</div>
            <a class="btn" href="/docs">Ver API / Changa</a>
            <a class="btn" href="/api" style="background:#4caf50">Ver JSON</a>
            <div class="dir">{TUCAN_DATA['direccion']}</div>
            <p style="margin-top:20px;font-size:12px">Hecho por Lana en San Miguel de Tucumán 🏔️</p>
        </div>
    </body>
    </html>
    """

@app.get("/api")
def api():
    return TUCAN_DATA

@app.get("/changa")
def changa():
    return {"mensaje": "¡Changa tucumana entregada!", "precio": TUCAN_DATA["precio"]}
