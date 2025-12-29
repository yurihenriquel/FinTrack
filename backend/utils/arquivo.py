import csv
from models.gasto import Gasto

class Arquivo:
    def __init__(self, caminho):
        self.caminho = caminho

    def salvar_gasto(self, gasto):
        with open(self.caminho, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                gasto.valor,
                gasto.categoria,
                gasto.data,
                gasto.descricao
            ])

    def ler_gastos(self):
        gastos = []
        try:
            with open(self.caminho, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for linha in reader:
                    gastos.append(Gasto.from_csv(linha))
        except FileNotFoundError:
            pass

        return gastos
    