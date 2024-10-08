import requests
from collections import Counter
import matplotlib.pyplot as plt

# Nome de usuário do GitHub
username = 'BiancaTacola'

# Obtém a lista de repositórios do usuário
url = f'https://api.github.com/users/{username}/repos'
response = requests.get(url)

# Verifica se a resposta da API foi bem-sucedida
if response.status_code != 200:
    print(f"Erro ao obter repositórios. Código de status: {response.status_code}")
    exit()

repos = response.json()

# Coleta informações sobre as linguagens usadas nos repositórios criados no 1º Semestre de 2024
languages_used = Counter()

for repo in repos:
    created_at = repo['created_at']

    if created_at.startswith('2024'):
        languages_url = repo['languages_url']
        repo_languages = requests.get(languages_url).json()

        for language in repo_languages.keys():
            languages_used[language] += 1

# Gera o gráfico de barras
labels, counts = zip(*languages_used.items())

plt.bar(labels, counts)

plt.ylabel('Quantidade de Projetos')
plt.title(f'Linguagens utilizadas em Repositórios Criados no 1º Semestre 2024 ({username})')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Caminho completo para o arquivo de imagem
caminho_arquivo = 'C:\\Bianca\\Bianca\\Alura\\Python_1\\grafico1_repositorios.png'

# Salva o gráfico como um arquivo de imagem
plt.savefig(caminho_arquivo)

# Exibe a mensagem indicando que o arquivo foi salvo com sucesso
print(f'O gráfico foi salvo em: {caminho_arquivo}')

# Exibe o gráfico
plt.show()

