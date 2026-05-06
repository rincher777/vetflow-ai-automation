from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="VetFlow AI - Smart Clinic API")

# Simulação de Banco de Dados de Insumos (Lógica FarmaStock)
inventory_db = {
    "vacina_v10": {"qtd": 5},
    "anti_rabica": {"qtd": 0},
    "consulta_geral": {"qtd": 999}
}

class AppointmentRequest(BaseModel):
    pet_name: str
    service: str
    date: str

@app.get("/")
def home():
    return {"status": "online", "message": "VetFlow AI Rodando"}

@app.post("/agendar")
async def check_and_book(request: AppointmentRequest):
    service_key = request.service.lower().replace(" ", "_")
    item = inventory_db.get(service_key)
    
    if not item or item["qtd"] <= 0:
        return {
            "status": "NEGADO",
            "message": f"Estoque insuficiente para {request.service}. Verifique o MedStock."
        }

    return {
        "status": "CONFIRMADO",
        "detalhes": f"Agendamento de {request.service} para o pet {request.pet_name} em {request.date}."
    }