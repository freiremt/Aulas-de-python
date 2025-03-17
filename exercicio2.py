import pandas as pd
import matplotlib.pyplot as plt

dados_paises = pd.read_csv('polucao.csv',delimiter=',')

plt.figure(figsize=(10, 6))

for paises in dados_paises['paises'].unique():
    dados_paises = dados_paises[dados_paises['paises'] == paises]
    plt.plot(dados_paises['ano'], dados_paises['valor'], label=paises, marker='o')

plt.title('Panorama da População de Mulheres no BR & EUA')
plt.xlabel('ano')
plt.ylabel('valor')
plt.legend(title='paises')
plt.legend(title='fonte: fao.org')

plt.grid(True)
plt.show()





#Mateus & Isaque