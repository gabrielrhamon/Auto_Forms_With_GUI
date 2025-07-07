import pyautogui
import time

# Instrução para o usuário
print("Movimente o mouse para ver as coordenadas. Pressione Ctrl+C para sair.")
pyautogui.moveTo(1,1)

try:
    
    while True:
        # Captura as coordenadas do mouse em tempo real
      
        x, y = pyautogui.position()
        print(f"Coordenadas do mouse: X={x} Y={y}", end='\r')  # O '\r' faz o texto sobrescrever na mesma linha
        time.sleep(0.1)  # Pausa de 100ms entre as atualizações

except KeyboardInterrupt:
    print("\nPrograma finalizado.")
