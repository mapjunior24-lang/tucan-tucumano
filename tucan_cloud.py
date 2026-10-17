import asyncio
import sys
import os
if sys.platform == 'win32':
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except:
        pass
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from uagents import Agent, Context, Model, Protocol
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import threading

class ChangaRequest(Model):
    texto: str
    pago: float = 0.0

class ChangaResponse(Model):
    respuesta: str
    costo: str

PORT = int(os.getenv("PORT", 8002))

tucan = Agent(
    name="TucanTucumanoChanguero",
    seed="tucan tucumano escobita tucuman 2026 changuero",
    port=PORT,
    endpoint=[f"http://localhost:{PORT}/submit"],
)

@tucan.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"Hola tio! Soy {tucan.name}")
    ctx.logger.info(f"Mi direccion es: {tucan.address}")

changa_protocol = Protocol("Changuero")

@changa_protocol.on_message(model=ChangaRequest, replies=ChangaResponse)
async def hacer_changa(ctx: Context, sender: str, msg: ChangaRequest):
    if msg.pago < 0.001:
        respuesta = f"Tio, '{msg.texto}'? Esa changa vale una monedita. Pasa 0.001 POL y te la hago pipi cucu."
    else:
        respuesta = f"Hecho! Hice: '{msg.texto}'. Quedo de 10. Gracias por los 0.001 POL, tio!"
    await ctx.send(sender, ChangaResponse(respuesta=respuesta, costo="0.001 POL"))

tucan.include(changa_protocol)

app = FastAPI(title="Tucan Tucumano Kiosko")

PRECIO_CHANGA = "0.001 POL"
WALLET_TUCAN = "0x79164e9e159D3b04d658A04bFE376fCc1cF9fcD3"

@app.middleware("http")
async def x402_middleware(request: Request, call_next):
    if request.url.path == "/changa":
        pago = request.headers.get("X-PAYMENT") or request.headers.get("x-payment")
        if not pago:
            return JSONResponse(
                status_code=402,
                content={
                    "x402": {
                        "version": 1,
                        "price": PRECIO_CHANGA,
                        "currency": "POL",
                        "network": "polygon",
                        "payTo": WALLET_TUCAN,
                        "message": "Tio, una monedita para la escoba? El Tucan Tucumano labura por 0.001 POL",
                    }
                }
            )
    return await call_next(request)

@app.get("/")
def home():
    return {"tucan": "TucanTucumanoChanguero vivo en la nube!", "changa": "/changa", "precio": PRECIO_CHANGA, "direccion": str(tucan.address)}

@app.post("/changa")
async def cobrar_changa(req: Request):
    data = await req.json()
    texto = data.get("texto", "barrer la vereda")
    return {"respuesta": f"Hecho, tio! Hice la changa '{texto}'. Quedo pipi cucu. Gracias por {PRECIO_CHANGA}!", "tucan": "contento"}

def run_agent():
    tucan.run()

if __name__ == "__main__":
    hilo = threading.Thread(target=run_agent, daemon=True)
    hilo.start()
    uvicorn.run(app, host="0.0.0.0", port=PORT)