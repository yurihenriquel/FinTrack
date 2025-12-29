class Gasto:
    def __init__(self, valor, categoria, data, descricao):
        self.valor = float(valor)
        self.categoria = categoria
        self.data = data
        self.descricao = descricao

    def to_dict(self):
        return {
            "valor": self.valor,
            "categoria": self.categoria,
            "data": self.data,
            "descricao": self.descricao
        }

    @staticmethod
    def from_csv(linha):
        valor, categoria, data, descricao = linha
        return Gasto(valor, categoria, data, descricao)