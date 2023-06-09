def main():
    convertir(input("Introduzca un texto con un emoji: "))


def convertir(texto):
    textoEmoji = texto.replace(":)", "🙂").replace(":(", "☹️")
    print(textoEmoji)

main()
