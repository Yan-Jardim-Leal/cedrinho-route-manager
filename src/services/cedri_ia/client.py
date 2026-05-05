from core import messages as m
from core.log import log
import httpx
from config import settings

CHECK_ENDPOINT = "/api/models/check"
CREATE_ENDPOINT = "/api/models/create"
HELLO_ENDPOINT = "/api/echo"
LOAD_ENDPOINT = "/api/models/load"
PROCESS_ENDPOINT = "/api/models/process"
TRAIN_ENDPOINT = "/api/models/train"
UNLOAD_ENDPOINT = "/api/models/unload"

HELLO_TIMEOUT = settings[m.HELLO_TIMEOUT]
DEFAULT_TIMEOUT = settings[m.DEFAUT_TIMEOUT]
BOT_INTERVAL = settings[m.BOT_INTERVAL]