# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define Heisenberg = Character("Heisenberg")

label start:
    scene fortnite
    pause
    show heisen
    pause
    Heisenberg "Meme nuevo a las 8pm no te lo pierdas"
    menu:
        "¿Que?":
            Heisenberg "tu no entiendes loco"
        "No":
            Heisenberg "ctm"
        "Sape meme nuevo":
            Heisenberg "Yo soy el peligro"
        "Ga?":
            Heisenberg "gaaaaa"

    return
