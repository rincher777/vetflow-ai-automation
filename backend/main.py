from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(title="OmniChannel AI Engine - Leomy Dev")

# --- BASE DE CONHECIMENTO COMPLETA ---
KKNOWLEDGE_BASE: Dict[str, Dict[str, str]] = {
    "veterinario": {
        "vacinacao": "Trabalhamos com V10, Raiva e Gripe. É necessário trazer a carteirinha do pet.",
        "castracao": "O procedimento exige jejum de 8h. O valor varia conforme o peso do animal.",
        "emergencia": "Nosso pronto-atendimento funciona até as 22h. Traga o animal imediatamente.",
        "banho_tosa": "Temos horários para banho e tosa nesta tarde. Gostaria de reservar?"
    },
    "estetica": {
        "lavieen": "O Lavieen é um laser de túlio para 'BB Laser', tratando poros e manchas. O protocolo padrão são 3 sessões.",
        "ultraformer": "O Ultraformer MPT é tecnologia de ponta para lifting facial sem cortes e quebra de gordura.",
        "botox": "A aplicação foca em rugas de expressão. O retoque é feito em 15 dias para garantir o resultado.",
        "pos_procedimento": "Após o laser, use protetor solar FPS 50+ a cada 3h e evite ácidos por 7 dias."
    },
    "odonto": {
        "limpeza": "A profilaxia inclui raspagem e polimento, essencial para evitar tártaro e gengivite.",
        "clareamento": "Oferecemos o clareamento de consultório (laser) e o caseiro com moldeiras personalizadas.",
        "implante": "O implante repõe o dente perdido com estética e função. Iniciamos com uma avaliação de RX.",
        "ortodontia": "Trabalhamos com aparelhos convencionais e alinhadores invisíveis. Agende sua moldagem."
    }
}

class WebhookPayload(BaseModel):
    nicho: str  # 'veterinario', 'estetica' ou 'odonto'
    procedimento: str
    nome_cliente: Optional[str] = "Cliente"

@app.post("/v1/atendimento")
async def processar_atendimento(payload: WebhookPayload):
    nicho_alvo = payload.nicho.lower()
    servico_alvo = payload.procedimento.lower()

    if nicho_alvo not in KNOWLEDGE_BASE:
        raise HTTPException(status_code=404, detail="Nicho não configurado.")

    info = KNOWLEDGE_BASE[nicho_alvo].get(
        servico_alvo, 
        "Vou confirmar os detalhes com a nossa equipe técnica e te retorno em instantes."
    )

    resposta_final = (
        f"Olá, {payload.nome_cliente}! ✨\n\n"
        f"Sobre o seu interesse em *{payload.procedimento.title()}*:\n"
        f"{info}\n\n"
        "Gostaria de agendar uma avaliação agora ou prefere tirar mais alguma dúvida?"
    )

    return {
        "success": True,
        "response_data": {"text": resposta_final}
    }

@app.get("/status")
async def check_status():
    return {"status": "online", "engine": "Leomy AI v2.0.0"}