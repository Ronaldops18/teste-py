# 1) Importar a classe
# "Calculadora"
from calculadoraIMC import CalculadoraIMC

# 2) Importar o pacote de
# testes unitários chamado "unittest"
import unittest



class TestCalculadoraIMC(unittest.TestCase):
    def setUp(self):
        self.calcIMC = CalculadoraIMC()

    def test_resultado(self):
        #testando o resultado para magreza
        self.assertEqual(self.calcIMC.resultado(60, 1.90), 'magreza')









# Executar a classe de
# testes unitários
if __name__ == '__main__':
    unittest.main()