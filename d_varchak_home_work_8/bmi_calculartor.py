class BMICalculator:
    def __init__(self):
        self.__height = 0.0
        self.__weight = 0.0


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    def __calculate_bmi(self) -> float | bool:
        try:
            return self.__weight / (self.__height ** 2)
        except ValueError:
            return False

    def __get_result_calculation_bmi(self):
        bmi = self.__calculate_bmi()
        match bmi:
            case b if b <= 16:
                return 'Выраженный дефицит массы тела'
            case b if b <= b < 18.5:
                return 'Недостаточная масса тела'
            case b if b <= 25:
                return 'Норма'
            case b if b <= 30:
                return 'Избыточная масса тела (предожирение)'
            case b if b <= 35:
                return 'Ожирение 1 степени'
            case b if b <= 40:
                return 'Ожирение 2 степени'
            case _:
                return 'Ожирение 3 степени (морбидное)'

    def get_report(self) -> str:
        """Полный отчет с данными и рекомендациями"""
        bmi = self.__calculate_bmi()
        category = self.__get_result_calculation_bmi()

        min_normal_weight = round(18.5 * (self.__height ** 2), 1)
        max_normal_weight = round(25 * (self.__height ** 2), 1)

        report = f"""
{'=' * 50}
ОТЧЕТ ПО ИНДЕКСУ МАССЫ ТЕЛА
{'=' * 50}
Рост: {self.__height} м
Вес: {self.__weight} кг
ИМТ: {bmi:.2f}
Категория: {category}

Нормальный вес для вашего роста: 
от {min_normal_weight} кг до {max_normal_weight} кг
{'=' * 50}
    """
        return report

def main():
    human_bmi: BMICalculator = BMICalculator()
    """Основная функция программы"""
    print("=" * 50)
    print("КАЛЬКУЛЯТОР ИНДЕКСА МАССЫ ТЕЛА (ИМТ)")
    print("=" * 50)
    print()

    while True:
        height = input("Введите ваш рост в метрах: ").replace(',', '.')
        weight = input("Введите ваш вес в кг: ").replace(',', '.')

        try:
            height_float = float(height)
            weight_float = float(weight)
            if not (0.5 <= height_float <= 3):
                print('Внимание: Рост должен быть от 0.5 до 3.0 метров!')
                continue
            if not (3 <= weight_float <= 400):
                print('Внимание: Вес должен быть от 3 до 400 кг!')
                continue

            break
        except ValueError:
            print('Введены не коректные данные, пожалуйста введите корректный рост и вес')

    human_bmi.height = height_float
    human_bmi.weight = weight_float
    print(human_bmi.get_report())

if __name__ == '__main__':
    main()