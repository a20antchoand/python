
def afegirTag (tag, text):
    generarTag = "<{0}>{1}</{0}>".format(tag, text)
    print(generarTag)

if __name__ == "__main__":
    tag = input("Indica el tag HTML: ")
    text = input("indica el text a mostrar: ")
    afegirTag(tag, text)