from datetime import datetime
import os
from typing import Dict

class Dashboard:


    COLORS = {
        'HEADER': '\033[95m',    # Purple
        'BLUE': '\033[94m',      # Blue
        'CYAN': '\033[96m',      # Cyan
        'GREEN': '\033[92m',     # Green
        'WARNING': '\033[93m',   # Yellow
        'FAIL': '\033[91m',      # Red
        'RESET': '\033[0m',      # Reset
        'BOLD': '\033[1m',       # Bold
        'DIM': '\033[2m'         # Dim
    }
    """Handles the display and tracking of bot statistics"""
    def __init__(self):
        self.stats = {
            'total_cycles': 0,
            'successful_cycles': 0,
            'failed_cycles': 0,
            'start_time': datetime.now(),
            'current_page': '',
            'last_action': '',
            'status': 'Running'
        }
        
    def clear_screen(self) -> None:
        """Clears the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def update_stats(self, **kwargs) -> None:
        """Updates statistics and refreshes display"""
        if 'total_cycles' in kwargs:
            kwargs['total_cycles'] = max(0, kwargs['total_cycles'] - 1)
        self.stats.update(kwargs)
        self.stats.update(kwargs)
        self.display()
        
    def display(self) -> None:
        """Displays the dashboard"""
        self.clear_screen()
        runtime = datetime.now() - self.stats['start_time']
        
        dashboard = f"""
{self.COLORS['DIM']}╔══════════════════════════════════════════════════════════════╗
{self.COLORS['DIM']}║{self.COLORS['RESET']}                     BOT IRIS DASHBOARD{self.COLORS['RESET']}{self.COLORS['DIM']}                       ║
{self.COLORS['DIM']}╠══════════════════════════════════════════════════════════════╣
{self.COLORS['DIM']}║ {self.COLORS['RESET']}Status: {self.stats['status']:<47}{self.COLORS['RESET']}{self.COLORS['DIM']}      ║
{self.COLORS['DIM']}║ {self.COLORS['RESET']}Runtime: {str(runtime).split('.')[0]:<46}{self.COLORS['RESET']}{self.COLORS['DIM']}      ║
{self.COLORS['DIM']}╠══════════════════════════════════════════════════════════════╣
{self.COLORS['DIM']}║ {self.COLORS['RESET']}Total Cycles: {self.stats['total_cycles']:<42}{self.COLORS['RESET']}{self.COLORS['DIM']}     ║
{self.COLORS['DIM']}║ {self.COLORS['RESET']}Successful:   {self.COLORS['GREEN']}{self.stats['successful_cycles']:<42}{self.COLORS['RESET']}{self.COLORS['DIM']}     ║
{self.COLORS['DIM']}║ {self.COLORS['RESET']}Failed:       {self.COLORS['FAIL']}{self.stats['failed_cycles']:<42}{self.COLORS['GREEN']}{self.COLORS['RESET']}{self.COLORS['DIM']}     ║
{self.COLORS['DIM']}╠══════════════════════════════════════════════════════════════╣
{self.COLORS['DIM']}║ {self.COLORS['RESET']}Current Page: {self.stats['current_page']:<42}{self.COLORS['RESET']}{self.COLORS['DIM']}     ║
{self.COLORS['DIM']}║ {self.COLORS['RESET']}Last Action:  {self.stats['last_action']:<42}{self.COLORS['RESET']}{self.COLORS['DIM']}     ║
{self.COLORS['DIM']}╚══════════════════════════════════════════════════════════════╝
{self.COLORS['RESET']}
"""
        print(dashboard)
# Initialize dashboard at the start of your scriptdashboard = Dashboard()def click_bot_iris(waiting_timer=3, cycle_count=0, start_time=None):    """Função principal para automatizar o preenchimento do formulário."""        if start_time is None:        start_time = time.time()    cycle_count += 1    dashboard.update_stats(        total_cycles=cycle_count,        current_page="Iniciando novo ciclo",        last_action="Preparando para começar"    )    # P R I M E I R A   P Á G I N A    dashboard.update_stats(current_page="Primeira Página", last_action="Verificando...")    if not check_correct_page("ref/01_page.png", confidence=0.9970):        dashboard.update_stats(failed_cycles=dashboard.stats['failed_cycles'] + 1, status="Erro na primeira página")        return cycle_count, start_time        dashboard.update_stats(last_action="Clicando em GO TO")    mouse_click(675, 923)    # Update the rest of your code similarly, adding dashboard updates at key points    # ...existing code...    # At the end of a successful cycle    dashboard.update_stats(        successful_cycles=dashboard.stats['successful_cycles'] + 1,        last_action="Ciclo completado com sucesso"    )    return cycle_count, start_timetry:    cycle_count = 0    start_time = time.time()    while True:        cycle_count, start_time = click_bot_iris(cycle_count=cycle_count, start_time=start_time)except KeyboardInterrupt:    dashboard.update_stats(status="Finalizado pelo usuário")    time.sleep(2)  # Give time to see the final status