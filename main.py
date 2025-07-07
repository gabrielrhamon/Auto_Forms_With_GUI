import pyautogui
import time
import random
import keyboard
from dataclasses import dataclass, field
from typing import List, Dict, Tuple
from dashboard import Dashboard

@dataclass
class Config:
    """Configuration constants for the application"""
    COLORS: Dict[str, str] = field(default_factory=lambda: {
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "DEFAULT": "\033[00m",
        "YELLOW": "\033[33m",
        "CYAN": "\033[36m"
    })
    
    LOCATIONS: List[str] = field(default_factory=lambda: [
        "Britagem de compactos", "Britagem secundária",
        "P.de armazenamento de materiais", "Terramesh",
        "Pátio de materiais"
    ])
    
    PROBLEMS: List[str] = field(default_factory=lambda: [
        'material com ausencia de organização',
        'malão de ferramenta desorganizado',
        'via sem sinalização',
        'Excesso de Particulado',
        'Dano na via'
    ])

class MouseController:
    """Handles mouse and keyboard interactions"""
    @staticmethod
    def click(x: int, y: int, interval: float = 0.15) -> None:
        pyautogui.click(x, y, interval=interval)
    
    @staticmethod
    def reset_position() -> None:
        pyautogui.moveTo(1, 1)
    
    @staticmethod
    def scroll_page(direction: str) -> None:
        if direction == 'down':
            pyautogui.press('pagedown', interval=0.2)
        elif direction == 'end':
            pyautogui.press('end', interval=0.3)
        elif direction == 'home':
            pyautogui.press('home', interval=0.2)
    
    @staticmethod
    def press_escape() -> None:
        pyautogui.press('esc')

class PageValidator:
    """Validates correct pages and handles page navigation"""
    def __init__(self, config: Config):
        self.config = config
        
    def check_page(self, image_path: str, confidence: float = 0.9995, max_retries: int = 250) -> bool:
        retries = 0
        while retries < max_retries:
            try:
                if pyautogui.locateOnScreen(image_path, confidence=confidence):
                    print(f"Página {self.config.COLORS['GREEN']}correta{self.config.COLORS['DEFAULT']} detectada:{image_path}", end='\r')
                    return True
                print("Página incorreta ou carregando... tentando novamente...", end='\r')
            except Exception:
                print(f"{self.config.COLORS['RED']}Tentando{self.config.COLORS['DEFAULT']} localizar a imagem: {image_path}. "
                      f"Tentativa {retries + 1}/{max_retries}", end='\r')
            retries += 1
            time.sleep(0.05)
        
        print(f"Erro: Não foi possível encontrar a página {image_path} após {max_retries} tentativas.")
        MouseController.press_escape()
        MouseController.click(120, 148)
        return False

class FormFiller:
    """Handles the form filling automation"""
    def __init__(self, config: Config, mouse: MouseController, validator: PageValidator):
        self.config = config
        self.mouse = mouse
        self.validator = validator
        self.dashboard = Dashboard()
        
    def fill_form(self, waiting_timer: float = 3, cycle_count: int = 0, start_time: float = None) -> Tuple[int, float]:
        if start_time is None:
            start_time = time.time()
        
        cycle_count += 1
        self.dashboard.update_stats(
            total_cycles=cycle_count,
            current_page="Iniciando ciclo",
            last_action="Preparando..."
        )
        
        time.sleep(waiting_timer/2)
        self.mouse.reset_position()

        # Process each page
        if not self._process_first_page():
            return cycle_count, start_time
        if not self._process_second_page():
            return cycle_count, start_time
        if not self._process_third_page():
            return cycle_count, start_time
        if not self._process_fourth_page():
            return cycle_count, start_time
        if not self._process_fifth_page():
            return cycle_count, start_time
        if not self._process_sixth_page():
            return cycle_count, start_time

        # Update successful completion
        self.dashboard.update_stats(
            successful_cycles=self.dashboard.stats['successful_cycles'] + 1,
            status="Ciclo completado com sucesso",
            last_action="Ciclo finalizado"
        )

        return cycle_count, start_time

    def _process_first_page(self) -> bool:
        self.dashboard.update_stats(
            current_page="Primeira Página",
            last_action="Verificando..."
        )
        if not self.validator.check_page("ref/01_page.png", confidence=0.9930):
            self.dashboard.update_stats(
                failed_cycles=self.dashboard.stats['failed_cycles'] + 1,
                status="Erro na primeira página"
            )
            return False
        
        self.dashboard.update_stats(last_action="Inicio do Reporte")
        self.dashboard.update_stats(current_page="Home")
        self.mouse.click(675, 923)
        return True
    
    def _process_second_page(self) -> bool:
        self.dashboard.update_stats(
            current_page="Segunda Página",
            last_action="Verificando..."
        )
        if not self.validator.check_page("ref/02_page.png", confidence=0.98):
            self.dashboard.update_stats(
                failed_cycles=self.dashboard.stats['failed_cycles'] + 1,
                status="Erro na segunda página"
            )
            return False
        
        self.dashboard.update_stats(last_action="Clicando em REPORTAR UM EVENTO")
        self.mouse.click(1660, 315)
        return True

    def _process_third_page(self) -> bool:
        self.dashboard.update_stats(
            current_page="Terceira Página",
            last_action="Verificando..."
        )
        # T E R C E I R A   P Á G I N A
        if not self.validator.check_page("ref/03_page.png", confidence=0.981):
            return False
        self.mouse.click(150, 600)  # TODAY
        self.mouse.click(120, 700)  # SELECT TIME OF EVENT
        self.mouse.click(120, 950)  # TYPE DESCRIPTION HERE...
        SELECTED_PROBLEM = random.choice(self.config.PROBLEMS)
        keyboard.write(SELECTED_PROBLEM)
        self.mouse.scroll_page('down')
        time.sleep(0.5)
        self.mouse.click(1200, 610)
        self.mouse.click(120, 780)  # LOCAL DESC.
        SELECTED_LOCATION = random.choice(self.config.LOCATIONS)
        keyboard.write(SELECTED_LOCATION)
        self.mouse.reset_position()

        self.mouse.click(1400, 880)  # NEXT
        self.mouse.reset_position()
        self.dashboard.update_stats(last_action="Clicando em NEXT na terceira página")
        return True

    def _process_fourth_page(self) -> bool:
        self.dashboard.update_stats(
            current_page="Quarta Página",
            last_action="Verificando..."
        )
        # Q U A R T A   P Á G I N A
        if not self.validator.check_page("ref/04_page.png", confidence=0.981):
            return False
        self.mouse.scroll_page('home')
        self.mouse.click(120, 740)  # PESSOAL
        self.mouse.click(120, 840)
        self.mouse.click(240, 950)
        self.mouse.scroll_page('end')
        self.mouse.click(120, 760)
        self.mouse.scroll_page('end')
        self.mouse.click(120, 760)  # AMBIENTAL
        self.mouse.click(120, 870)
        self.mouse.scroll_page('end')
        self.mouse.click(120, 760)  # MATERIAL
        self.mouse.click(120, 870)
        self.mouse.click(120, 980)
        self.mouse.scroll_page('end')
        self.mouse.click(120, 760)   # SOCIAL
        self.mouse.click(120, 870)  

        self.mouse.click(1388, 956)  # NEXT
        return True

    def _process_fifth_page(self) -> bool:
        self.dashboard.update_stats(
            current_page="Quinta Página",
            last_action="Verificando..."
        )
        # Q U I N T A    P Á G I N A
        if not self.validator.check_page("ref/05_page.png", confidence=0.988):
            return False
        self.mouse.scroll_page('home')
        self.mouse.click(125, 685)  # CATEG.
        self.mouse.scroll_page('home')
        self.mouse.click(155, 820)
        self.mouse.scroll_page('end')
        self.mouse.click(845, 195)
        self.mouse.click(1370, 880)
        return True

    def _process_sixth_page(self, waiting_timer: float = 3) -> bool:
        self.dashboard.update_stats(
            current_page="Sexta Página",
            last_action="Verificando..."
        )
        # S E X T A    P Á G I N A
        time.sleep(waiting_timer/2)
        if not self.validator.check_page("ref/06_page.png", confidence=0.989):
            return False
        self.mouse.click(240, 635)  # INFO
        self.mouse.click(120, 740)
        self.mouse.click(240, 870)
        self.mouse.click(120, 965)
        self.mouse.scroll_page('end')
        self.mouse.click(240, 820)
        self.mouse.click(120, 930)
        self.mouse.scroll_page('end')
        self.mouse.click(120, 730)
        self.mouse.click(240, 880)
        self.mouse.click(120, 965)
        self.mouse.scroll_page('end')
        self.mouse.click(240, 440)

        keyboard.write('Realizado Adequação')

        self.mouse.click(120, 640)
        self.mouse.click(120, 730)
        self.mouse.click(120, 955)
        self.mouse.click(1400, 1012)
        return True

        # Calcular tempo total
        elapsed_time = time.time() - start_time
        print(f"\nCiclo {self.config.COLORS['YELLOW']}{cycle_count}{self.config.COLORS['DEFAULT']} "
              f"executado em {self.config.COLORS['CYAN']}{elapsed_time:.2f}{self.config.COLORS['DEFAULT']} segundos")

        return cycle_count, start_time

def main():
    config = Config()
    mouse = MouseController()
    validator = PageValidator(config)
    form_filler = FormFiller(config, mouse, validator)
    
    cycle_count = 0
    start_time = time.time()
    
    try:
        while True:
            cycle_count, start_time = form_filler.fill_form(
                cycle_count=cycle_count, 
                start_time=start_time
            )
    except KeyboardInterrupt:
        form_filler.dashboard.update_stats(
            status="Finalizado pelo usuário",
            last_action="Programa encerrado"
        )
        time.sleep(2)
    except Exception as e:
        form_filler.dashboard.update_stats(
            status=f"Erro: {str(e)}",
            last_action="Erro crítico"
        )
        time.sleep(2)
        raise

if __name__ == "__main__":
    main()