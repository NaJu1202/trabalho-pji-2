from fastapi import FastAPI
from pydantic import BaseModel

from src.db.connection import ConnectionDB  # sua classe

app = FastAPI()
db = ConnectionDB()


class VacinaIn(BaseModel):
    nome: str
    grupo: str
    pais: str


class PaisesIn(BaseModel):
    nome: str


@app.get("/paises")
def listar_paises():
    resultado = db.controler_pais.consultar_paises()
    return {"paises": resultado}


@app.get("/vacinas")
def pesquisar_vacinas(pais: str):
    resultado = db.controler_vacinas.pesquisar_vacinas_por_pais(nome_pais=pais)

    return {pais: resultado}


@app.post("/vacinas")
def cadastrar_vacina(vacina: VacinaIn):
    db.controler_vacinas.cadastrar_vacina(
        nome_vacina=vacina.nome, grupo_de_risco=vacina.grupo, pais=vacina.pais
    )
    return {"mensagem": "Vacina cadastrada com sucesso"}
