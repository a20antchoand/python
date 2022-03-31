if __name__ == '__main__':

    mylist = []
    cont = 0
    continuar = True

    while continuar == True:
        mylist += input("Introduce un numero: ")

        if len(mylist) == 8:
            continuar = False

    print("Llista: ", mylist)

    while len(mylist) > 5:
        mylist.pop(4)
        print("Llista: ", mylist)


