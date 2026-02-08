import random
import time

TASK_PULL = [
    "Прибрать квартиру",
    "Проверить трубы",
    "Напугать жильцов",
    "Покормить собаку"
]
PLACES_PULL = [101,102,103,104,105]
day = []

def generate_day():
    day = []
    place_pull = [PLACES_PULL[random.randint(0, len(PLACES_PULL) - 1)] for i in range(random.randint(3, 7))]
    for place in place_pull:
        day.append({place: TASK_PULL[random.randint(0, len(TASK_PULL) - 1)]})
    return day

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time} сек.")
        return result
    return wrapper

def print_day(day):
    for task_and_place in day:
        for place, task in task_and_place.items():
           print(f"Задача: {task}, квартира: {place}")
def start_day():
    global day
    if len(day) != 0:
        print("День уже начат")
        return
    day = generate_day()

def complete_task(place, task):
    global day
    if {int(place):task} in day:
       day.remove({int(place): task})
       print("Задача выполнена!")
    else:
       print("Ошибка в написании задачи или квартиры")
       print(f"Задач осталось {len(day)}")
@timer
def complete_day():
    global day
    if len(day) == 0:
        print("День не начат")
        return
    while len(day) != 0:
        print_day(day)
        place, task = input("Введите через запятую квартиру и задачу: ").split(",")
        complete_task(place, task.strip())
        print("День завершен")

methods = {
    "Начать день": start_day,
    "Выполнить день": complete_day,
    "Выход": lambda:exit(0)
}

while True:
    for methods_name in methods.keys():
        print(methods_name)
    chose = input("Выберите действие: ")
    if chose not in methods.keys():
       continue
    methods[chose]()
