from console_ui import clear_ui, display_output, handle_keypress
from controler import get_random_puzzle


def main():
    """Fonction principale de l'application"""
    try:
        # Récupération d'un taquin tiré aléatoirement
        puzzle = get_random_puzzle()

        while True:
            # Attend une action et affiche le résultat
            puzzle = handle_keypress(puzzle)
            display_output(puzzle)

    except KeyboardInterrupt:
        pass
    finally:
        # Lorsqu'on quite, on restaure l'environnement du terminal
        clear_ui()


if __name__ == "__main__":
    main()
