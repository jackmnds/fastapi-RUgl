from fastapi import FastAPI, Request


app = FastAPI()


@app.api_route('/webhook', methods=['POST'])
async def listener(request: Request):
    contrato = await request.json()
    print(contrato)
