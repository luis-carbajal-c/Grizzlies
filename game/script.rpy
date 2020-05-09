# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define Heisenberg = Character("Heisenberg")

label start:

    $ you = name()
    scene fortnite
    pause
    show heisen
    pause
    Heisenberg "DoTa"
    menu:
        "DoTa":
            Heisenberg "sape"
        "No":
            Heisenberg "ctm"
    return
