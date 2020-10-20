from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn
import random
import svc10
import buses
app = FastAPI()

@app.get("/buslocation/")
async def root(code: str, key: str):
    if key == "V&cfDSOMAB@%!ZZ2GCN5O@gpz2p$3KO9lctw48zo":
        return {
            "Bus_Code": code,
            "Current_Location": svc10.stopSeq[random.randint(0, len(svc10.stopSeq) - 1)]
        }
    else:
        item={
            "detail":"Incorrect API Key"
        }
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=item)

@app.get("/buscall/{busstop}")
async def root(busstop: str, key: str, svc: str, num: str):
    if key == "FG2E74FZe1JqLL1qm4GSLMNNhXMAempBTzcPy7J9":
        busesSent = []
        for i in range (int(num)):
            busnum = buses.busplates[random.randint(0, len(buses.busplates) - 1)]
            buses.busplates.remove(busnum)
            # msg = "Bus number " + busnum + " of service " + svc + " has been called"
            # print('\033[33;1m' + msg, '\033[m')
            busesSent.append(busnum)
        return {
            "message": "Bus number " + str(busesSent) + " of service " + svc + " have been sent.",
            "Data": {
                "Bus_Number": busesSent,
                "Calling_Bus_Stop": busstop,
                "Svc": svc
            }
        }
    else:
        item={
            "detail":"Incorrect API Key"
        }
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=item)

