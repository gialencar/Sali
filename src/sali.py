

class Sali:

    inss_tabela = [
        [1100.00],
        [1100.01, 2203.48],
        [2203.49, 3305.22],
        [3305.23, 6433.57]
        ]

    irrf_tabela = [
        [1903.98],
        [1903.99, 2826.65],
        [2826.66, 3751.05],
        [3751.06, 4664.68]
    ]

    def inss_calc(self, salario_bruto):

        if (salario_bruto <= self.inss_tabela[0][0]):
            inss = salario_bruto * 0.075
            rendimento = salario_bruto - inss

        elif (self.inss_tabela[1][0] <= salario_bruto <= self.inss_tabela[1][1]):
            inss = salario_bruto * 0.09 - 16.50
            rendimento = salario_bruto - inss

        elif (self.inss_tabela[2][0] <= salario_bruto <= self.inss_tabela[2][1]):
            inss = salario_bruto * 0.12 - 82.60
            rendimento = salario_bruto - inss

        elif (self.inss_tabela[3][0] <= salario_bruto <= self.inss_tabela[3][1]):
            inss = salario_bruto * 0.14 - 148.70
            rendimento = salario_bruto - inss

        else:
            inss = 751.97
            rendimento = salario_bruto - inss

        # print(f'rendimento: R$ {rendimento:.2f}')
        return round(inss, 2)

    def irrf_calc(self, rendimento):

        if (rendimento <= self.irrf_tabela[0][0]):
            irrf = 0
            salario_liquido = rendimento

        elif (self.irrf_tabela[1][0] <= rendimento <= self.irrf_tabela[1][1]):
            irrf = rendimento * 0.075 - 142.80
            salario_liquido = rendimento - irrf

        elif (self.irrf_tabela[2][0] <= rendimento <= self.irrf_tabela[2][1]):
            irrf = rendimento * 0.15 - 354.80
            salario_liquido = rendimento - irrf

        elif (self.irrf_tabela[3][0] <= rendimento <= self.irrf_tabela[3][1]):
            irrf = rendimento * 0.225 - 636.13
            salario_liquido = rendimento - irrf

        else:
            irrf = rendimento * 0.275 - 869.36
            salario_liquido = rendimento - irrf

        # print(f'Salário líquido: R$ {salario_liquido:.2f}')
        return round(irrf, 2)


def main():

    sali = Sali()
    bruto = float(input("Salário bruto: "))
    inss = sali.inss_calc(bruto)
    rendimento = bruto - inss
    irrf = sali.irrf_calc(rendimento)
    msc = bruto * 0.17
    liquido = rendimento - irrf

    verde = "\033[32m"
    vermelho = "\033[31m"
    reset = "\033[0m"

    print(f"INSS                    -R$ {vermelho}{inss:.2f}{reset}")
    print(f"IRRF                    -R$ {vermelho}{irrf:.2f}{reset}")
    print(f"Salário líquido          R$ {verde}{liquido:.2f}{reset}")
    print(f"Salário líquido(MSC)     R$ {verde}{liquido - msc:.2f}{reset}")

if __name__ == "__main__":
    main()