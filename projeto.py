import math

class Minimizar_Cabo:
    def __init__(self, custo_terra, custo_rio, largura_rio, distancia_fabrica):
        self.custo_terra = custo_terra
        self.custo_rio = custo_rio
        self.largura_rio = largura_rio
        self.distancia_fabrica = distancia_fabrica
    
    def calcular_custo(self, x):
        distancia_rio = math.sqrt(x**2 + self.largura_rio**2)
        distancia_terra = self.distancia_fabrica - x
        custo_total = (distancia_rio * self.custo_rio) + (distancia_terra * self.custo_terra)
        return custo_total, distancia_rio, distancia_terra

    def calcular(self):
        if self.custo_rio > self.custo_terra:
            x_otimizado = math.sqrt((self.custo_terra**2 * self.largura_rio**2) / 
                                     (self.custo_rio**2 - self.custo_terra**2))
        else:
            x_otimizado = self.distancia_fabrica  
        return self.calcular_custo(x_otimizado)

    @staticmethod
    def from_input():
        while True:
            try:
                largura_rio = float(input("\n\nQual é a largura do rio (em metros): ").replace(",", "."))
                if largura_rio < 0:
                    raise ValueError("A largura do rio não pode ser negativa!")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                distancia_fabrica = float(input("\nQual é a distância da fábrica ao rio (em metros): ").replace(",", "."))
                if distancia_fabrica < 0:
                    raise ValueError("A distância não pode ser negativa!")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                custo_rio = float(input("\nQual é o custo por metro pelo rio? ").replace(",", "."))
                if custo_rio < 0:
                    raise ValueError("O custo por metro pelo rio não pode ser negativo!")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                custo_terra = float(input("\nQual é o custo por metro pela terra? ").replace(",", "."))
                if custo_terra < 0:
                    raise ValueError("O custo por metro pela terra não pode ser negativo!")
                break
            except ValueError as e:
                print(e)

        return Minimizar_Cabo(custo_terra, custo_rio, largura_rio, distancia_fabrica)
    
    def exibir_resultados(self):
        custo_total, distancia_rio, distancia_terra = self.calcular()

        print("\nResultados obtidos:")
        print(f"\t\nDistância percorrida pelo rio: {distancia_rio:.2f} m")
        print(f"\t\nDistância percorrida pela terra: {distancia_terra:.2f} m")
        print(f"\t\nMenor custo total de transporte: R$ {custo_total:.2f}")