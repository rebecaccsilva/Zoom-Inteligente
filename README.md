# 🔍 Zoom Inteligente

> Um script Python que detecta automaticamente quando você está assistindo a um vídeo com a tela dividida ao meio e ajusta o zoom do navegador para melhorar a visualização.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

---

## 💡 Sobre o projeto

Quem estuda com aula em um lado da tela e o material em outro sabe: o vídeo quase sempre fica pequeno demais para ler o que está sendo mostrado. O **Zoom Inteligente** resolve isso automaticamente.

O script monitora a janela ativa em segundo plano e, quando percebe que ela:
- está com a largura equivalente à metade da tela, **e**
- o título contém o nome de um serviço de vídeo (YouTube, Netflix, Twitch, Globoplay, Prime Video, Stremio, Curso em Vídeo...),

ele aplica automaticamente um zoom-out no navegador para exibir mais conteúdo em menos espaço. Quando a janela volta ao tamanho normal ou o vídeo é fechado, o zoom é resetado sozinho.

## ⚙️ Como funciona

1. Obtém a largura do monitor principal.
2. A cada 1,5 segundo, verifica qual é a janela ativa.
3. Compara a largura da janela com a metade da tela (com margem de tolerância).
4. Verifica se o título da janela contém algum serviço de vídeo conhecido.
5. Se as duas condições forem verdadeiras, aplica `Ctrl -` algumas vezes via automação de teclado.
6. Quando a condição deixa de ser válida, restaura o zoom para 100% (`Ctrl 0`).

## 📦 Tecnologias e bibliotecas

- `pygetwindow` — identifica a janela ativa e suas dimensões
- `pyautogui` — simula os atalhos de teclado de zoom
- `screeninfo` — detecta a resolução do monitor principal
- `rich` — deixa os logs do terminal mais legíveis

## 🚀 Como usar

```bash
# Clone o repositório
git clone https://github.com/rebecaccsilva/Zoom-Inteligente.git
cd Zoom-Inteligente

# Instale as dependências
pip install pygetwindow pyautogui screeninfo rich

# Rode o script
python zoom_inteligente.py
```

Depois de iniciado, basta deixar o script rodando em segundo plano e usar o navegador normalmente — o zoom é ajustado sozinho sempre que a tela dividida com vídeo for detectada.

## 🎯 O que eu pratiquei aqui

- Automação de interface (simulação de teclado e leitura de janelas ativas)
- Loops de monitoramento contínuo com tratamento de exceções
- Lógica condicional para detectar padrões de uso reais

---

<p align="center">Feito por <a href="https://github.com/rebecaccsilva">Rebeca Silva</a> 💻</p>
