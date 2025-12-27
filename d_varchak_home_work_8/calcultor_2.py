class Calculator:
    def __init__(self) -> None:
        self._number_a = 0.0
        self._number_b = 0.0
        self._operator = ''

    @property
    def number_a(self) -> float:
        return self._number_a
    @property
    def number_b(self) -> float:
        return self._number_b

    @number_a.setter
    def number_a(self, number_a: float) -> None:
        self._number_a = number_a

    @number_b.setter
    def number_b(self, number_b: float) -> None:
        self._number_b = number_b

    @property
    def operator(self) -> str:
        return self._operator

    @operator.setter
    def operator(self, operator: str) -> None:
        self._operator = operator

    def calculate(self) -> float:
        try:
            match self._operator:
                case '+':
                    return self._number_a + self._number_b
                case '-':
                    return self._number_a - self._number_b
                case '*':
                    return self._number_a * self._number_b
                case '/':
                    return self._number_a / self._number_b
        except ZeroDivisionError:
            print('Делить на ноль нельзя!!!!')
            return float('inf')

    def get_report(self):

        result = f"""
{'=' * 50}
РЕЗУЛЬТАТ ОПЕРАЦИИ
{self.number_a} {self._operator} {self.number_b} = {self.calculate():.4f}
{'=' * 50}        
    """
        return result



def main():
    calculator  = Calculator()
    """Основная функция программы"""
    print("=" * 50)
    print("КАЛЬКУЛЯТОР")
    print("=" * 50)
    print()

    while True:
        number_a = input("Введите число a: ").replace(',', '.')
        number_b = input("Введите число b: ").replace(',', '.')
        operator = input('Введите оператор "+", "-", "*", "/": ')

        try:
            number_a_float = float(number_a)
            number_b_float = float(number_b)
            if operator not in ["+", "-", "*", "/"]:
                print('Внимание: оператор должен быть одним из "+", "-", "*", "/"!')
                continue

            break
        except ValueError:
            print('Введены не коректные данные, пожалуйста введите корректные значения')

    calculator.number_a = number_a_float
    calculator.number_b = number_b_float
    calculator.operator = operator
    result = calculator.get_report()
    print(result)


if __name__ == '__main__':
    main()