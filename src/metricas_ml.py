import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score, f1_score


def plot_confusion_matrix(cm, labels, title):
    """Dibuja la matriz de confusión como mapa de calor."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        cm, annot=True, fmt='d', cmap='Blues',
        xticklabels=labels, yticklabels=labels, ax=ax
    )
    ax.set_title(title)
    ax.set_ylabel('Etiqueta real')
    ax.set_xlabel('Etiqueta predicha')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def resumen_metricas(y_true, y_pred):
    """Devuelve un diccionario con las métricas resumen."""
    return {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Macro F1': f1_score(y_true, y_pred, average='macro'),
        'Weighted F1': f1_score(y_true, y_pred, average='weighted')
    }