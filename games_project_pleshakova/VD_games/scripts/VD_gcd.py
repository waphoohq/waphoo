import random
from games_project_pleshakova.VD_games.cli import welcome_user, get_user_answer


def gcd(a, b):
    """Вычисляет наибольший общий делитель двух чисел."""
    while b != 0:
        a, b = b, a % b
    return a


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    
    correct_answers = 0
    total_questions = 3
    
    while correct_answers < total_questions:
        # Генерируем случайные числа
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        
        # Показываем вопрос
        print(f'Question: {a} {b}')
        
        # Получаем ответ от пользователя
        user_answer = get_user_answer()
        
        # Вычисляем правильный ответ
        correct_answer = str(gcd(a, b))
        
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
