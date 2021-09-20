import abc
from unittest import TestCase, main

class Calculadora(object):
    def calcula(self, valor1, valor2, operador):
        operationFabrica = OperacaoFabrica()
        operation = operationFabrica.criar(operador)
        if operation == None:
            return 0
        else:
            result = operation.executar(valor1, valor2)
            return result


class OperacaoFabrica(object):

    def cria(self, operador):
        if operador == 'soma':
            return Soma()
        elif operador == 'subtracao':
            return Subtracao()
        elif operador == 'divisao':
            return Divisao()
        elif operador == 'multiplicacao':
            return Multiplicacao()
        else: 
            return None

class Operacao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executa(self, valor1, valor2):
        pass
    
class Soma(Operacao):
    def executa(self, valor1, valor2):
        resul = valor1 + valor2
        return result
    
class Subtracao(Operacao):
    def executa(self, valor1, valor2):
        result = valor1 - valor2
        return result

class Multiplicacao(Operacao):
    def executa(self, valor1, valor2):
        result = valor1 * valor2
        return result

class Divisao(Operacao):
    def executa(self, valor1, valor2):
        if valor2 == 0:
            return 'impossivel dividir por 0'
        result = valor1 / valor2
        return result

class Testes(TestCase):

    def test_soma(self):
        calculation = Calculadora()
        result = calculation.calcula(2,3,'soma')
        self.assertEqual(result, 5)
    
    def test_subtracao(self):
        calculation = Calculadora()
        result = calculation.calcula(2,4,'subtracao')
        self.assertEqual(result, -2)
    
    def test_multiplicacao(self):
        calculation = Calculadora()
        result = calculation.calcula(2,5,'multiplicacao')
        self.assertEqual(result, 10)

    def test_divisao(self):
        calculation = Calculadora()
        result = calculation.calcula(4,2,'divisao')
        self.assertEqual(result, 2)

    def test_operacao(self):
        calculation = Calculadora()
        result = calculation.calcula(4,2, 'subtrair')
        self.assertEqual(result, 0)

    def test_divisao_por_zero(self):
        calculation = Calculadora()
        result = calculation.calcula(5,0, 'divisao')
        self.assertEqual(result, 'impossivel dividir por 0')


    
calculation = Calculadora()
calcula = calculation.calcula(5,5, 'soma')
print("RESULTADO:", calcula)


if __name__ == '__main__':
    main()