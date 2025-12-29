class RelatorioEstatistico:

    @staticmethod
    def total(gastos):
        return sum(g.valor for g in gastos)

    @staticmethod
    def media(gastos):
        if not gastos:
            return 0
        return sum(g.valor for g in gastos) / len(gastos)

    @staticmethod
    def total_por_categoria(gastos):
        categorias = {}
        for g in gastos:
            categorias[g.categoria] = categorias.get(g.categoria, 0) + g.valor
        return categorias