def init():
    n = int(input("Ingrese el número n: "))
    strng = ""

    for i in range(0, n):
        for j in range(0, n):
            strng += "*"
        strng += "\n"


    print(strng)

if __name__ == "__main__":
    init()
