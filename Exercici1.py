
if __name__ == '__main__':

    mylist = []
    cont = 0
    continuar = True

    while continuar == True:
        mylist += input("Introduce un numero: ")

        print(len(mylist))

        if len(mylist) == 5:
            continuar = False

    for i in mylist:
        if int(i) % 2 == 0:
            cont = cont + 1

    print("Numeros pars: ", cont)
