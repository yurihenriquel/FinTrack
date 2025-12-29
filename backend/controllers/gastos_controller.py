from models.gasto import Gasto
from utils.arquivo import Arquivo
from services.relatorio import RelatorioEstatistico

class GastosController:
    def __init__(self):
        self.arquivo = Arquivo("backend/data/gastos.csv")

    def adicionar_gasto(self, data):
        gasto = Gasto(
            valor=data.get("valor"),
            categoria=data.get("categoria"),
            data=data.get("data"),
            descricao=data.get("descricao")
        )

        self.arquivo.salvar_gasto(gasto)
        return {"status": "sucesso", "mensagem": "Gasto cadastrado!"}

    def listar_gastos(self):
        gastos = self.arquivo.ler_gastos()
        return [g.to_dict() for g in gastos]

    def estatisticas(self):
        gastos = self.arquivo.ler_gastos()
        stats = {
            "total": RelatorioEstatistico.total(gastos),
            "media": RelatorioEstatistico.media(gastos),
            "por_categoria": RelatorioEstatistico.total_por_categoria(gastos)
        }
        return stats