import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


# Загружаем датасет Iris
IrisData = load_iris()
data = IrisData.data   # Определяем входные данные
target = IrisData.target   # Определяем целевые данные

# Разделяем данные на обучающий и тестовый наборы
data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.2, random_state=42)

# Создаём нейронную сеть
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(data_train.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(3, activation='softmax'))
# Компилируем и обучаем модель нейронной сети
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(data_train, target_train, epochs=50, batch_size=32, validation_split=0.1)

# Оцениваем точность нейросети на тестовом наборе данных
test_loss, test_accuracy = model.evaluate(data_test, target_test)
print(f'Точность: {test_accuracy:.4f}')

# Получаем предсказания нейросети для тестового набора данных
predictions = model.predict(data_test)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = target_test

# Инициализируем матрицу ошибок
conf_matrix = confusion_matrix(true_classes, predicted_classes)
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Матрица ошибок')
plt.colorbar()

# Добавляем метки на график
tick_marks = np.arange(len(IrisData.target_names))
plt.xticks(tick_marks, IrisData.target_names, rotation=45)
plt.yticks(tick_marks, IrisData.target_names)
plt.xlabel('Прогноз')
plt.ylabel('Истина')

# Отображаем график
plt.show()
