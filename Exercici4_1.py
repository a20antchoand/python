def decimalToRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    numero = int(number)

    resultat = []


    while numero:
        div = numero // num[i]
        numero %= num[i]

        while div:
            resultat.append(sym[i])
            div -= 1
        i -= 1

    print(resultat)

if __name__ == "__main__":
    number = input("Indica el numero en decial: ")
    print("Numero romá:")
    decimalToRoman(number)