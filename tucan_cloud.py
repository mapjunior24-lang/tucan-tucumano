from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
from datetime import datetime

app = FastAPI()

# TU BILLETERA - ACA TE LLEGA LA PLATA
MI_BILLETERA = "0x79164e9e159D3b04d658A04bFE376fCc1cF9fcD3"
PRECIO = "0.001 POL"
RED = "Polygon Amoy / Polygon Mainnet"

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

@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>Tucan Tucumano - Oficial</title>
    <style>
        body{{font-family:sans-serif;background:#fff8e1;text-align:center;padding:20px;}}
        .card{{background:white;border-radius:20px;padding:30px;max-width:480px;margin:0 auto;box-shadow:0 10px 30px rgba(0,0,0,0.15);}}
        .tucan{{font-size:80px;}} h1{{color:#ff6f00;}} 
        .precio{{font-size:20px;background:#ffecb3;padding:12px;border-radius:10px;margin:15px 0; border:2px dashed #ff6f00;}}
        .wallet{{font-size:11px;word-break:break-all;background:#f5f5f5;padding:8px;border-radius:8px;}}
        .btn{{display:block;background:#ff6f00;color:white;padding:15px;border-radius:10px;text-decoration:none;font-weight:bold;margin:10px 0;}}
        input{{padding:12px;width:80%;border-radius:10px;border:2px solid #ff6f00;margin:10px 0;}}
    </style></head>
    <body><div class="card">
        <div class="tucan">🦜</div><h1>Tucan Tucumano</h1>
        <p><b>Saludo + Copla tucumana con tu nombre</b><br>¡100% automático!</p>
        <div class="precio">💰 {PRECIO} - Paga y recibis al instante</div>
        <p><b>Mi billetera oficial:</b></p><div class="wallet">{MI_BILLETERA}</div>
        <form action="/changa" method="get">
            <input name="nombre" placeholder="Escribi tu nombre..." required>
            <input name="tx" placeholder="Pega aqui el Hash de tu pago (0x...)" style="border-color:green">
            <button class="btn" type="submit" style="border:none;width:100%;cursor:pointer;background:green;">¡Ya pagué, quiero mi copla!</button>
        </form>
        <a class="btn" href="/pagar" style="background:#4caf50">1. ¿Como pagar? Click aca</a>
        <a class="btn" href="/api" style="background:#2196F3">API para Agentes</a>
        <p style="font-size:11px;color:#888;">Hecho por Lana en SMT - Venta automatica 24/7</p>
    </div></body></html>
    """

@app.get("/pagar", response_class=HTMLResponse)
def pagar():
    return f"""
    <html><body style='font-family:sans-serif;text-align:center;padding:20px;background:#fff8e1;'>
    <div style='background:white;padding:30px;border-radius:20px;max-width:500px;margin:0 auto;'>
    <h1>💸 Como pagar al Tucan</h1>
    <p>1. Abri tu Metamask</p>
    <p>2. Red: <b>Polygon</b></p>
    <p>3. Envia <b>{PRECIO}</b> a:</p>
    <p style='word-break:break-all;background:#eee;padding:10px;border-radius:10px;'><b>{MI_BILLETERA}</b></p>
    <p>4. Copia el Hash de la transaccion (Tx Hash)</p>
    <p>5. Volve al inicio y pegalo junto a tu nombre</p>
    <a href='/' style='display:block;background:#ff6f00;color:white;padding:15px;border-radius:10px;text-decoration:none;margin-top:20px;'>Volver y reclamar copla</a>
    </div></body></html>
    """

@app.get("/changa")
def changa(nombre: str = "changuito", tx: str = ""):
    if not tx or len(tx) < 10:
        return {
            "error": "Falta el pago chango!",
            "instruccion": f"Primero paga {PRECIO} a {MI_BILLETERA}",
            "paso_1": "Anda a /pagar para ver como pagar",
            "paso_2": "Luego llama de nuevo a /changa?nombre={nombre}&tx=TU_HASH",
            "estado": "Esperando pago"
        }
    
    saludo = random.choice(SALUDOS)
    copla = generar_copla(nombre)
    return {
        "para": nombre,
        "saludo": f"{saludo} Soy el Tucan y te saludo, {nombre}!",
        "copla": copla,
        "regalo": "¡Que nunca falte la empanada!",
        "pago_recibido": tx,
        "verificado": "Pago registrado - Gracias por tu compra!",
        "precio": PRECIO,
        "vendedor": MI_BILLETERA,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api")
def api():
    return {
        "agente": "TucanTucumano",
        "billetera": MI_BILLETERA,
        "precio": PRECIO,
        "red": RED,
        "como_comprar": "/changa?nombre=TuNombre&tx=HashDelPago",
        "instrucciones_pago": "/pagar",
        "descripcion": "Agente automatico que vende saludos y coplas tucumanas 24/7"
    }
