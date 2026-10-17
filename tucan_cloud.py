from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
from datetime import datetime

app = FastAPI()

COPLAS = [
    "En San Miguel de Tucuman, donde el lapacho florecio, {nombre} paso por aca y el Tucan lo saludo.",
    "Si vas pa' la Quebrada, llevate un recuerdo fiel, que {nombre} es buena gente y el Tucan lo sabe bien.",
    "Con empanada y vino patero, te canto esta cancion, para {nombre} va mi copla, salida del corazon.",
    "Tucuman, tierra querida, jardin de la Republica, {nombre} que Dios te bendiga, con zamba y chacarera.",
    "En el cerro San Javier, donde brilla el sol, {nombre} dejo su nombre, con amor y fulgor."
]

SALUDOS = ["¡Ahaaa chango!", "¡Que viva Tucuman!", "¡Bienvenido a mi rancho!", "¡Echale ganas!"]

def generar_copla(nombre: str):
    plantilla = random.choice(COPLAS)
    return plantilla.format(nombre=nombre)

TUCAN_DATA = {
    "tucan": "TucanTucumanoChanguero vivo en la nube!",
    "precio": "0.001 POL",
    "servicio": "Saludo + Copla tucumana",
    "direccion": "agent1qvs9087jse6d4c2hhyKj5x2d4z1q6g9yc1cwwX2zdkjns3228xa1ta16e"
}

@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <!DOCTYPE html>
    <html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tucan Tucumano</title>
    <style>
        body{{font-family:sans-serif;background:#fff8e1;text-align:center;padding:20px;}}
        .card{{background:white;border-radius:20px;padding:30px;max-width:450px;margin:0 auto;box-shadow:0 10px 30px rgba(0,0,0,0.1);}}
        .tucan{{font-size:80px;}} h1{{color:#ff6f00;}}
        .precio{{font-size:20px;background:#ffecb3;padding:12px;border-radius:10px;margin:15px 0;}}
        .btn{{display:block;background:#ff6f00;color:white;padding:15px;border-radius:10px;text-decoration:none;font-weight:bold;margin:10px 0;}}
        input{{padding:12px;width:80%;border-radius:10px;border:2px solid #ff6f00;margin:10px 0;}}
    </style></head>
    <body><div class="card">
        <div class="tucan">🦜</div><h1>Tucan Tucumano</h1>
        <p><b>Saludo + Copla tucumana con tu nombre</b></p>
        <div class="precio">💰 {TUCAN_DATA['precio']} - Entrega inmediata</div>
        <form action="/changa" method="get">
            <input name="nombre" placeholder="Escribi tu nombre..." required>
            <button class="btn" type="submit" style="border:none;width:100%;cursor:pointer;">¡Quiero mi copla!</button>
        </form>
        <a class="btn" href="/api" style="background:#4caf50">Ver API para Agentes</a>
        <p style="font-size:11px;color:#888;">Hecho por Lana en SMT</p>
    </div></body></html>
    """

@app.get("/changa")
def changa(nombre: str = "changuito"):
    saludo = random.choice(SALUDOS)
    copla = generar_copla(nombre)
    return {
        "para": nombre,
        "saludo": f"{saludo} Soy el Tucan y te saludo, {nombre}!",
        "copla": copla,
        "regalo": "¡Que nunca falte la empanada!",
        "precio": TUCAN_DATA["precio"],
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api")
def api():
    return {"agente": TUCAN_DATA, "como_comprar": "GET /changa?nombre=TuNombre", "descripcion": "Saludos tucumanos automaticos"}
