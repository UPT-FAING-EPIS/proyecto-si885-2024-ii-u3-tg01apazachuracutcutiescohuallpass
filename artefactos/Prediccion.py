import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

dataset = dataset[['`dia`', '`total_mbps`']]

dataset['`total_mbps`'] = pd.to_numeric(dataset['`total_mbps`'], errors='coerce')

dia_mapping = {
    'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3, 
    'Viernes': 4, 'Sábado': 5, 'Domingo': 6
}
dataset['`dia_num`'] = dataset['`dia`'].map(dia_mapping)

X = dataset[['`dia_num`']]
y = dataset['`total_mbps`']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Error cuadrático medio (MSE): {mse}")

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Valores reales')
plt.plot(X_test, y_pred, color='red', label='Predicción', linewidth=2)
plt.title('Predicción de Total Mbps según el Día')
plt.xlabel('Día de la Semana')
plt.ylabel('Total Mbps')
plt.xticks(range(7), ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
plt.legend()
plt.grid(True)

plt.show()

dataset['predicción_mbps'] = model.predict(dataset[['`dia_num`']])
print("Dataset con predicciones:")
print(dataset)

dataset
