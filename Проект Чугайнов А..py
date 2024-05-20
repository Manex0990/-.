from random import randint


class MyMath:
    def generate_square_x(self):
        """
        Вернет кв уравнение в строковом формате
        """
        self.a_sq = randint(-3, 5)
        self.b_sq = randint(-11, 11)
        self.c_sq = randint(-11, 11)
        if self.a_sq == 0:
            self.a_sq = 1
        elif self.b_sq == 0:
            self.b_sq = 1
        elif self.c_sq == 0:
            self.c_sq = 1

        if self.b_sq == 1:
            if self.c_sq < 0:
                return f'{self.a_sq}x\u00B2 + x - {-self.c_sq} = 0'
            else:
                return f'{self.a_sq}x\u00B2 + x + {self.c_sq} = 0'

        elif self.b_sq == -1:
            if self.c_sq < 0:
                return f'{self.a_sq}x\u00B2 - x - {-self.c_sq} = 0'
            else:
                return f'{self.a_sq}x\u00B2 - x + {self.c_sq} = 0'

        if self.b_sq < 0 and self.c_sq > 0:
            sq_x = f'{self.a_sq}x\u00B2 - {-self.b_sq}x + {self.c_sq} = 0'
        elif self.b_sq > 0 and self.c_sq < 0:
            sq_x = f'{self.a_sq}x\u00B2 + {self.b_sq}x - {-self.c_sq} = 0'
        elif self.b_sq < 0  and self.c_sq < 0:
            sq_x = f'{self.a_sq}x\u00B2 - {-self.b_sq}x - {-self.c_sq} = 0'
        else:
            sq_x = f'{self.a_sq}x\u00B2 + {self.b_sq}x + {self.c_sq} = 0'

        if self.a_sq == 1:
            sq_x = sq_x[1:]
        elif self.a_sq == -1:
            sq_x = f'-{sq_x[2:]}'
        return sq_x

    def answer_square_x(self):
        """
        Вернет 1) если дискриминант положительный - список из 2 целых или дробных чисел
                  2) если дискриминант 0 - одно целое или дробное число
                  3) если дискриминант отрицательный - строку "Корней нет"
           корни последнего сгенерированного кв уравнения
           """
        d = (abs(self.b_sq) ** 2) - (4 * self.a_sq * self.c_sq)
        if d == 0:
            self.answer = (-self.b_sq) / (2 * self.a_sq)
            return self.answer

        elif d > 0:
            x1 = (-self.b_sq - d ** 0.5) / (2 * self.a_sq)
            x2 = (-self.b_sq + d ** 0.5) / (2 * self.a_sq)
            if isinstance(x1, int) and not isinstance(x2, int):
                self.answer = sorted([x1, round(x2, 2)])
            elif isinstance(x2, int) and not isinstance(x1, int):
                self.answer = sorted([round(x1, 2), x2])
            elif isinstance(x1, int) and isinstance(x2, int):
                self.answer = sorted([x1, x2])
            elif not isinstance(x1, int) and not isinstance(x2, int):
                self.answer = sorted([round(x1, 2), round(x2, 2)])
            return self.answer

        else:
            self.answer = 'Корней нет'
            return self.answer

    def check_answer_square_x(self, user_answer):
        """
        В качестве ответа может быть принято
        1) 2 корня кв уравнения через пробел(это могут быть целые числа или дробные(округлите до сотых) числа)
        2) один корень - целое чило или дробное(округлите до сотых) число
        3) строка 'Корней нет'
        """
        if user_answer == 'Корней нет':
            if str(self.answer_square_x()) == user_answer:
                return 'Верно'
            else:
                return f'Неверно. Правильный ответ {self.answer_square_x()}.'

        elif isinstance(user_answer, int) or isinstance(user_answer, float):
            if float(user_answer) == float(self.answer_square_x()):
                return 'Верно'
            else:
                return f'Неверно. Правильный ответ {self.answer_square_x()}.'

        temp = [float(i) for i in user_answer.split(' ')]
        if sorted(temp) == list(self.answer_square_x()):
            return 'Верно'
        else:
            return f'Неверно. Правильный ответ {self.answer_square_x()}.'

    def generate_line_x(self):
        """
        Вернет линейное уравнение в строковом формате
        """
        self.a_li = randint(-11, 11)
        self.b_li = randint(-11, 11)
        self.c_li = randint(-11, 11)

        if self.b_li < 0:
            line_x = f'{self.a_li}x - {-self.b_li} = {self.c_li}'
        elif self.b_li > 0:
            line_x = f'{self.a_li}x + {self.b_li} = {self.c_li}'
        elif self.b_li == 0:
            self.b_li = 1
            line_x = f'{self.a_li}x + {self.b_li} = {self.c_li}'

        if self.a_li == 1 or self.a_li == 0:
            self.a_li = 1
            line_x = line_x[1:]
        elif self.a_li == -1:
            line_x = f'-{line_x[2:]}'
        return line_x

    def answer_line_x(self):
        """
        Вернет корень последнего сгенерированного линейного уравнения
        """
        temp = self.c_li + (-self.b_li)
        if temp / self.a_li == temp // self.a_li:
            self.x = temp // self.a_li
        else:
            self.x = round(temp / self.a_li, 2)
        return self.x

    def check_answer_line_x(self, user_answer):
        """
        В качестве ответа может быть принято
        целое число или дробное(округлите до сотых) число
        """
        if float(user_answer) == float(self.answer_line_x()):
            return 'Верно'
        else:
            return f'Неверно. Правильный ответ {self.answer_line_x()}.'

    def generate_sum(self):
        """
        Вернет пример на сложение в строковом формате
        """
        self.a_s = randint(1, 101)
        self.b_s = randint(1, 101)
        return f'{self.a_s} + {self.b_s} = ?'

    def answer_sum(self):
        """
        Вернет решение последнего сгенерированного примера на сложение
        """
        return self.a_s + self.b_s

    def check_answer_sum(self, user_answer):
        """
        В качестве ответа принимается целое число
        """
        if float(self.answer_sum()) == float(user_answer):
            return 'Верно'
        else:
            return f'Неверно. Правильный ответ {self.answer_sum()}.'

    def generate_min(self):
        """
        Вернет пример на вычитание в строковом формате
        """
        self.a_m = randint(1, 101)
        self.b_m = randint(1, 101)
        return f'{self.a_m} - {self.b_m} = ?'

    def answer_min(self):
        """
        Вернет решение последнего сгенерированного примера на вычитание
        """
        return self.a_m - self.b_m

    def check_answer_min(self, user_answer):
        """
        В качестве ответа принимается целое число или вещественное число
        """
        if float(self.answer_min()) == float(user_answer):
            return 'Верно'
        else:
            return f'Неверно. Правильный ответ {self.answer_min()}.'

    def generate_crop(self):
        """
        Вернет пример на деление в строковом формате
        """
        self.a_cr = randint(1, 51)
        self.b_cr = randint(1, 51)
        return f'{self.a_cr} / {self.b_cr} = ?'

    def answer_crop(self):
        """
        Вернет решение последнего сгенерированного примера на деление
        """
        if self.a_cr / self.b_cr == self.a_cr // self.b_cr:
            return self.a_cr // self.b_cr
        else:
            return round(self.a_cr / self.b_cr, 2)

    def check_answer_crop(self, user_answer):
        """
        В качестве ответа принимается целое число или дробное(округлите до сотых) число
        """
        if float(self.answer_crop()) == float(user_answer):
            return 'Верно'
        else:
            return f'Неверно. Правильный ответ {self.answer_crop()}.'

    def generate_multiply(self):
        """
        Вернет пример на умножение в строковом формате
        """
        self.a_mul = randint(1, 21)
        self.b_mul = randint(1, 21)
        return f'{self.a_mul} * {self.b_mul} = ?'

    def answer_multiply(self):
        """
        Вернет решение последнего сгенерированного примера на умножение
        """
        return self.a_mul * self.b_mul

    def check_answer_multiply(self, user_answer):
        """
        В качестве ответа принимается целое число
        """
        if float(self.answer_multiply()) == float(user_answer):
            return 'Верно'
        else:
            return f'Неверно. Правильный ответ {self.answer_multiply()}.'


print('Здравствуйте. Эта программа может помочь в подготовке к экзамену по алгебре.')
print('Она может сгенерировать и проверить:')
print('1) Квадратное уравнение(square)')
print('2) Линейное уравнение(line_x)')
print('3) Пример на сложение(sum)')
print('4) Пример на вычитание(min)')
print('5) Пример на умножение(multiply)')
print('6) Пример на деление(crop)')
print('Если возникнут вопросы можно использовать функцию help()')
print('Выберите, что хотите решить.')
print('Для этого введите цифру соответствующего задания.')
number = input()

math = MyMath()
pos = ''


def verify(ans, type, msg):
    try:
        ans = type(ans)
        return ans
    except:
        print(msg)


while pos != 'STOP':
    if number == '1':
        print(math.generate_square_x())
        print('Введите ответ')
        print('1) если 2 корня => введите корни через пробел в любом порядке(десятичные дроби округлите до сотых)')
        print('2) если 1 корень => введите корень(если он дробный окгрулите до сотых)')
        print('3) если нет корней => введите фразу "Корней нет"')
        answer = input()
        if answer != 'Корней нет' or (not isinstance(answer, int) or not isinstance(answer, float)) or len(answer.split(' ')) != 2:
            print('Не распознано.')
            print('Завершение работы.')
            break
        else:
            print(math.check_answer_square_x(answer))
    elif number == '2':
        print(math.generate_line_x())
        print('Введите корень линейного уравнения')
        answer = input()
        ans = verify(answer, float, 'Не распознано. Завершение работы.')
        if not ans:
            break
        else:
            print(math.check_answer_line_x(answer))
    elif number == '3':
        print(math.generate_sum())
        print('Введите ответ')
        answer = input()
        ans = verify(answer, float, 'Не распознано. Завершение работы.')
        if not ans:
            break
        else:
            print(math.check_answer_sum(answer))
    elif number == '4':
        print(math.generate_min())
        print('Введите ответ')
        answer = input()
        ans = verify(answer, float, 'Не распознано. Завершение работы.')
        if not ans:
            break
        else:
            print(math.check_answer_min(answer))
    elif number == '5':
        print(math.generate_multiply())
        print('Введите ответ')
        answer = input()
        ans = verify(answer, float, 'Не распознано. Завершение работы.')
        if not ans:
            break
        else:
            print(math.check_answer_multiply(answer))
    elif number == '6':
        print(math.generate_crop())
        print('Введите ответ')
        answer = input()
        ans = verify(answer, float, 'Не распознано. Завершение работы.')
        if not ans:
            break
        else:
            print(math.check_answer_crop(answer))
    else:
        print('Команда не распознана.')
    print('Хотите попробовать ещё? Напишите "да" или "нет".')
    ans = input()
    if ans.lower() == 'да':
        print('Выберите, что хотите решить.')
        print('Для этого введите цифру соответствующего задания.')
        number = input()
    elif ans.lower() == 'нет':
        pos = 'STOP'
        print('Завершение работы.')
    else:
        print('Команда не распознана.')
        pos = 'STOP'
        print('Завершение работы.')
