import httpx
from core import messages as m
from core.log import log
from core import constants

MODEL_ENDPOINT = "/api/models/create"
MODEL = {
  "architecture": {
    "layers": [
      {
        "activation": "relu",
        "input_shape": [
          10
        ],
        "type": "Dense",
        "units": 64
      },
      {
        "activation": "linear",
        "type": "Dense",
        "units": 2
      }
    ]
  },
  "learning_type": "supervised",
  "training_config": {
    "learning_rate": 0.001,
    "loss_function": "mse",
    "optimizer": "adam"
  }
}

def createModel(config):
    url = f"http://{config[m.IPIA]}:{config[m.PORTIA]}{MODEL_ENDPOINT}"
    
    try:
        log(f"Requesting route from IA Manager: {url}")
        response = httpx.post(url, timeout=constants.DEFAULT_TIMEOUT, json=MODEL)
        response.raise_for_status()
        
        log(f"Success! IA Manager responded with route: {response.json()}")
        return response.json().get("token")
    except httpx.HTTPStatusError as exc:
        log(f"HTTP error on IA (Status {exc.response.status_code}) on solicitation {exc.request.url}.",2)
        return None
    except httpx.RequestError as exc:
        log(f"Failure {exc.request.url}. The IA Manager it's turned on?",3)
        return None