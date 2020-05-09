
init python:
    def name():
        while True:
            name = renpy.input("que hago ñaño")
            name = name.strip()
            if name != "":
                return name
