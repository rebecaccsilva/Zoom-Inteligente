import time
import pygetwindow as gw
import pyautogui
from screeninfo import get_monitors
from rich import print

appli_com_video= ["Youtube", "Netflix","Twitch","Globoplay","Prime Video","Stremio","Curso em Video"]
cliques_zoom= 4


def largura_da_tela():
    '''
    Pega a largura do monitor principal
    '''
    for m in get_monitors():
        if m.is_primary:
            return m.width
    return 1920 #valor padrão caso falhe


def checar_e_ajustar_zoom():
    largura_tela= largura_da_tela()
    largura_metade= largura_da_tela/2

    zoom_aplicado=False

    print(':robot: Script Iniciado. Monitorando suas janelas...')
    
    while True:
        try:
            # Pega a janela que está em primeiro plano (ativa)
            janela_ativa= gw.getActiveWindow()

            if janela_ativa is not None and janela_ativa.title != "":
                titulo = janela_ativa.title
                largura_janela= janela_ativa.width

                # Verifica se a janela está dividida (com margem de erro de 100px)
                esta_na_metade= abs(largura_janela - largura_metade)<100

                # Verifica se o título da janela corresponde a um vídeo
                tem_video= any(palavra.lower() in titulo.lower() for palavra in appli_com_video)

                # Aplica a lógica de automação
                if esta_na_metade and tem_video and not zoom_aplicado:
                    print(f":clapper_board: Vídeo detectado na metade da tela: '{titulo}'. Ajustando o zoom...")

                    # Reseta o zoom para o padrão (Ctrl + 0)
                    pyautogui.hotkey('ctrl','0')
                    time.sleep(0.2)
                    pyautogui.hotkey('ctrl','-')
                    time.sleep(0.1)

                    # Aplica o zoom out (Ctrl + -) a quantidade de vezes configurada
                    for _ in range(cliques_zoom):
                        pyautogui.hotkey('ctrl','+')
                        time.sleep(0.05)

                    zoom_aplicado=True
                
                # Se o usuário maximizar a tela ou fechar o vídeo, o zoom volta ao normal
                elif (not esta_na_metade or not tem_video) and zoom_aplicado:
                    print(":arrows_clockwise: Janela normalizada. Resetando zoom para 90%...")
                    pyautogui.hotkey('ctrl','0')
                    zoom_aplicado=False

        except Exception as e:
            # Previne que o script feche caso você clique em uma janela do sistema (como a barra de tarefas)
            pass

        time.sleep(1.5)

if __name__ == "__main__":
    checar_e_ajustar_zoom()