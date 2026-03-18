import random
from games_project_pleshakova.VD_games.cli import welcome_user, get_user_answer


def calculate(a, b, operator):
    """Вычисляет результат математической операции."""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    
    correct_answers = 0
    total_questions = 3
    operators = ['+', '-', '*']
    
    while correct_answers < total_questions:
        # Генерируем случайные числа и оператор
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        operator = random.choice(operators)
        
        # Показываем вопрос
        print(f'Question: {a} {operator} {b}')
        
        # Получаем ответ от пользователя
        user_answer = get_user_answer()
        
        # Вычисляем правильный ответ
        correct_answer = str(calculate(a, b, operator))
        
        # Проверяем ответ
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
