import random


def uzmninešana():
    skaitlis = random.randint(1, 10)
    print("Uzmini skaitli no 1 līdz 10!")
    uzm_skaitlis = int(input("num: "))
    if uzm_skaitlis == skaitlis:
        print("Pareizi!!!!!!!!")
    else:
        print("Diemžēl nepareizi")


def atkartošana():
    print("Vai gribi atkartot?")
    izvele = str(input())

print("Ievadi savu vārdu:")
vards = input()
print("Svecināts", vards,"!")

while True:
    uzmninešana()
    print("Vai gribi atkartot?")
    izvele = str(input())
    if izvele.lower() == "ne":
        break


    