
init python:
    def name():
        while True:
            name = renpy.input("Ingresa tu nombre")
            name = name.strip()
            if name != "":
                return name
