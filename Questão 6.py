class BombaCombustivel:
    # Tipo Combustível: 1 - Álcool, 2 - Gasolina
    def __init__(self,qtde_combustivel=0, tipo_combustivel=1):
        self.tipo_combustivel = tipo_combustivel
        self.qtde_combustivel = qtde_combustivel
        self.valor_litro = 3.19

    def abastecer_por_valor(self, valor):
        qnt = valor / self.valor_litro
        if qnt > self.qtde_combustivel:
            return False
        self.qtde_combustivel -= qnt
        return qnt

    def abastecer_por_litro(self, litro):
        if litro > self.qtde_combustivel:
            return False
        self.qtde_combustivel -= litro
        return self.valor_litro * litro

    def alterar_valor(self, valor):
        self.valor_litro = valor
        return True

    def consultar_valor(self):
        return self.valor_litro

    def alterar_combustivel(self, tipo):
        self.tipo_combustivel = tipo
        if self.tipo_combustivel == 1:
            self.valor_litro = 3.19
            return True
        elif self.tipo_combustivel == 2:
            self.valor_litro = 4.91
            return True
        else:
            return False

    def recarregar_bomba(self):
        self.qtde_combustivel += 10000
        return True
