import pandas as pd

# Импортируем датасет в программу
dataset = pd.read_csv('Preferences.csv')
# Определяем список жанров, из которых будем вычислять самый популярный
genres = {"Dance", "Folk", "Country", "Classical music", "Musical", "Pop", "Rock", "Metal or Hardrock", "Punk", "Hiphop, Rap", "Reggae, Ska", "Swing, Jazz", "Rock n roll", "Alternative", "Latino", "Techno, Trance", "Opera"}


# Принимает список жанров и датасет
def getMostPopularGenre(genres, data):
    # Инициализируем пустой словарь, в котором будет хранить рейтинг каждого жанра
    rating = {}
    # Для каждого жанра вычисляем среднюю оценку и добавляем в словарь, округляя до 2-ух знаков после запятой
    for genre in genres:
        rating[genre] = round(data[genre].mean(), 2)

    # Возвращает строку - ключ с самым большим значением из словаря
    return max(rating, key = rating.get)    


# Принимает датасет
def getLivingInBlockOfFlats(data):
    # Получаем абсолютное количество людей, живших в многоквартирном доме
    absolute = data[data['House - block of flats'] == 'block of flats'].shape[0]
    # Получаем процент
    percent = absolute / data.shape[0] * 100

    # Возвращает строку - процент людей, живших в многоквартирном доме
    return f'{round(percent)}%'


# Принимает датасет
def getFiltered(data):
    # Этап 1 - получаем людей, заинтересованных игрой на инструментах
    step1 = data[data['Musical instruments'] >= 4]
    # Этап 2 - из них получаем тех, кто никогда не курил
    step2 = step1[step1['Smoking'] == 'never smoked']
    # Этап 3 - из них получаем тех, кто никогда не пил
    step3 = step2[step2['Alcohol'] == 'never']

    # Возвращает целое число - количество людей, которые заинтересованы игрой на инструментах И не курят И не пьют
    return step3.shape[0]


if __name__ == '__main__':
    # Записываем необходимые данные в переменные
    mostPopularGenre = getMostPopularGenre(genres, dataset)
    livingInBlockOfflats = getLivingInBlockOfFlats(dataset)
    filtered = getFiltered(dataset)

    # Выводим данные в консоль
    print(
        f'Самый популярный жанр: {mostPopularGenre}\n'
        f'Процент живших в многоквартирном доме: {livingInBlockOfflats}\n'
        f'Кол-во играющих на инструментах, не курящих и не пьющих: {filtered}'
    )
    