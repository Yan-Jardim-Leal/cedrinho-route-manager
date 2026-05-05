from core import messages
from core.log import log
import httpx
import time
import token

HELLO_TIMEOUT = 5.0
BOT_INTERVAL = 3 # seconds between bot routes # 1 hour default

PROCESS_TEST = {
  "input": [
    1.5,
    2.3,
    0.8
  ],
  "session_id": "session-XYZ-123",
  "token": ""
}

def run(config):
    log(f"Route Manager running. {messages.IPIA}:{messages.PORTIA}")
    url = f"http://{messages.IPIA}:{messages.PORTIA}/api/echo"
    
    try:
        log(f"Sending hello requests to: {url}")

        response = httpx.get(url, timeout=HELLO_TIMEOUT)
        response.raise_for_status()
        
        log(f"Success! IA Manager responded: {response.json()}")
        return True

    except httpx.HTTPStatusError as exc:
        log(f"HTTP error on IA (Status {exc.response.status_code}) on solicitation {exc.request.url}.",2)
        return False
    except httpx.RequestError as exc:
        log(f"Failure {exc.request.url}. The IA Manager it's turned on?",3)
        return False
    
def stop():
    pass

def routeLoop(config):
    config[messages.TOKEN] = token.getToken(config)
    while config[messages.RUNNING]:
        route = getRoute(config)
        if route:
            log(f"Received new route: {route}")
        else:
            log("Failed to get a new route.", 2)
        
        time.sleep(BOT_INTERVAL)

def readyToProcess(config):
    """Checks if the Route Manager is ready to start processing routes."""

    
    
    return True

def getRoute(config):

    token = config[messages.TOKEN]
    url = f"http://{messages.IPIA}:{messages.PORTIA}{MODEL_ENDPOINT}"

    payload = PROCESS_TEST.copy()
    payload["token"] = token

    try:
        log(f"Requesting route from IA Manager: {url}")
        response = httpx.post(url, timeout=HELLO_TIMEOUT, json=payload)
        response.raise_for_status()
        
        log(f"Success! IA Manager responded with route: {response.json()}")
        return response.json().get("route")
    except httpx.HTTPStatusError as exc:
        log(f"HTTP error on IA (Status {exc.response.status_code}) on solicitation {exc.request.url}.",2)
        return None
    except httpx.RequestError as exc:
        log(f"Failure {exc.request.url}. The IA Manager it's turned on?",3)
        return None

    pass



