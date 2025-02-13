import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # Valores corretos
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]  # Valores previstos pelo modelo

conf_matrix = confusion_matrix(y_true, y_pred)

def exibir_matriz_confusao(matrix):
    TN, FP, FN, TP = matrix.ravel()
    P = TP/(TP+FP)
    N = 10
    S = TN/(TN+FN) 
    print(f" Verdadeiro Negativo (VN): {TN}")
    print(f" Falso Positivo (FP): {FP}")
    print(f" Falso Negativo (FN): {FN}")
    print(f" Verdadeiro Positivo (VP): {TP}")
    print(f" Sensibilidade: {S}")
    print(f" Especificidade: {TN/(FP+TN)}")
    print(f" Acurácia: {(TP+TN)/N}")
    print(f" Precisão: {P}")
    print(f" F-score: {2*((P*S)/(P+S))}")

print("Matriz de Confusão:\n", conf_matrix)
exibir_matriz_confusao(conf_matrix)

plt.figure(figsize=(5, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Negativo (0)", "Positivo (1)"],
            yticklabels=["Negativo (0)", "Positivo (1)"])
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão")
plt.show()

