import time
import pygetwindow as gw
import pyautogui
from screeninfo import get_monitors

appli_com_video = [
    "youtube",
    "netflix",
    "twitch",
    "globoplay",
    "prime video",
    "stremio",
    "curso em video",
    "curso em vídeo",
    "curso de python",
    "aula de python",
    "video",
]

programas_para_ignorar = [
    "visual studio code",
    "vscode",
    "prompt de comando",
    "cmd",
    "explorador de arquivos",
    "bloco de notas",
    "minecraft",
    "code",
    "launcher",
]
cliques_zoom = 4


def largura_da_tela():
    """
    Pega a largura do monitor principal
    """
    for m in get_monitors():
        if m.is_primary:
            return m.width
    return 1920  # valor padrão caso falhe


def checar_e_ajustar_zoom():
    largura_tela = largura_da_tela()
    largura_metade = largura_tela / 2

    zoom_aplicado = False

    while True:
        try:
            # Pega todas as janelas visíveis no Windows
            todas_janelas = gw.getAllWindows()

            janela_video_encontrada = None

            # Procura se existe alguma janela de vídeo em meia tela aberta em algum lugar
            for janela in todas_janelas:
                if janela.title != "" and not janela.isMinimized:
                    titulo = janela.title.lower()

                    # Ignora programas de código logo de cara
                    if any(prog in titulo for prog in programas_para_ignorar):
                        continue

                    # Verifica se é uma janela de vídeo e se está em meia tela
                    esta_na_metade = abs(janela.width - largura_metade) < 100
                    tem_video = any(palavra in titulo for palavra in appli_com_video)

                    if esta_na_metade and tem_video:
                        janela_video_encontrada = janela
                        break  # Encontrou o vídeo em meia tela, pode parar de procurar

            # SE ENCONTROU UM VÍDEO EM MEIA TELA E O ZOOM NÃO FOI APLICADO AINDA
            if janela_video_encontrada and not zoom_aplicado:
                janela_atual = (
                    gw.getActiveWindow()
                )  # Guarda onde você está clicado agora

                # Ativa a janela do vídeo rapidinho só para aplicar o zoom nela
                janela_video_encontrada.activate()
                time.sleep(0.2)

                # Aplica o zoom
                pyautogui.hotkey("ctrl", "0")
                time.sleep(0.15)
                pyautogui.hotkey("ctrl", "-")
                time.sleep(0.15)
                for _ in range(cliques_zoom):
                    pyautogui.hotkey("ctrl", "+")
                    time.sleep(0.05)

                zoom_aplicado = True

                # Devolve o foco para onde você estava para você não perder o clique
                if janela_atual:
                    try:
                        janela_atual.activate()
                    except Exception:
                        pass

            # SE NÃO HÁ MAIS NENHUM VÍDEO EM MEIA TELA, MAS O ZOOM AINDA CONSTA COMO ATIVO
            elif not janela_video_encontrada and zoom_aplicado:
                # Significa que você fechou o vídeo ou maximizou ele
                for janela in todas_janelas:
                    titulo = janela.title.lower()
                    # Procura o navegador
                    if any(
                        p in titulo for p in ["chrome", "edge", "firefox", "opera"]
                    ) or any(v in titulo for v in appli_com_video):
                        try:
                            janela_atual = gw.getActiveWindow()
                            janela.activate()
                            time.sleep(0.2)
                            pyautogui.hotkey("ctrl", "0")
                            time.sleep(0.15)
                            pyautogui.hotkey("ctrl", "-")
                            if janela_atual:
                                janela_atual.activate()
                            break
                        except Exception:
                            pass
                zoom_aplicado = False

        except Exception as e:
            pass
        time.sleep(2)


if __name__ == "__main__":
    checar_e_ajustar_zoom()
