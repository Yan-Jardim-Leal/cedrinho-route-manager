import argparse
import uvicorn

from fastapi import FastAPI, HTTPException

import api.route_manager as route_manager
import services.data_manager as data_manager
from services import auth_token
from config import settings

from schemas.data import ModelDataValidator, ModelDataResponse

from core import messages as m
from core.log import log


active_models = {}
active_sessions = {}

# ==========================================
#       MAIN APPLICATION
# ==========================================


async def lifespan(app: FastAPI):
    log.setVerbose()
    log(f"starting with Verbose Mode ON...")
    log(f"[settingsurações de Rede: PORT={settings[m.PORT]}]")
    log(f"[settingsurações da IA: IP={settings[m.IPIA]}, PORT={settings[m.PORTIA]}]")
    log("Starting Server...",0)

    auth_token.run()
    route_manager.run()
    data_manager.run()
    
    yield
    log("Stopping Server...")

app = FastAPI(
    title="CEDRI Route Manager",
    description="REST API for the CEDRI Route Manager from IPB",
    version="2.0.0",
    lifespan=lifespan
)

# ==========================================
#       ROTAS REST
# ==========================================

@app.get("/api/echo")
async def echo_route():
    return {"message": "[S] Ai manager loaded."}

@app.post("/api/models/send-data", status_code=200, response_model=ModelDataResponse)
async def send_data(payload: ModelDataValidator):
    """Model data endpoint, receives the model data and accumulates it for further processing."""
    result = data_manager.sendData(payload.model_dump())
    return result

# ==========================================
#       INICIALIZAÇÃO E ARGPARSE
# ==========================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CEDRI AI Manager Startup Script")
    
    parser.add_argument("-v", "--verbose", action="store_true", help="Activate detailed loggings.")
    parser.add_argument("--port", type=int, default=48001, help="Server port")
    parser.add_argument("--ipia", type=str, default="0.0.0.0", help="Communication IP with the AI")
    parser.add_argument("--portia", type=int, default=48000, help="Communication port with the AI")
    parser.add_argument("--new", action="store_true", help="Create a new model model_token, ignoring existing ones.")

    args = parser.parse_args()

    settings[m.VERBOSE] = args.verbose
    settings[m.PORT] = args.port
    settings[m.IPIA] = args.ipia
    settings[m.PORTIA] = args.portia
    settings[m.NEW] = args.new
    
    uvicorn.run(app, host="0.0.0.0", port=args.port)