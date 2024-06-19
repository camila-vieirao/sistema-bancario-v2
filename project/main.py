from usuarios import menu_inicio
from sistema import menu_operacoes_bancarias

if __name__ == "__main__":
    usuario = menu_inicio()
    menu_operacoes_bancarias(usuario)