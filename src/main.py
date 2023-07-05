import counter as c
import sys as s

def options() -> str:
    m = input("1) Konzol bemenet\n2) Fájlból olvasás\nOpció: ")
    while m != "1" and m != "2":
        m = input("1) Konzol bemenet\n2) Fájlból olvasás\nOpció: ")
    return m

def from_file(filename: str):
    res = not c.check_format(filename)
    if res:
        c.modify(filename)
        
    data = c.read_from_file(filename)
    if data != []:
        c.counting(data)
    else:
        print("Hiba: Üres fájl")

def run() -> None:
    print("\nÜdvözöl a kreditindex számoló!\n")

    n = len(s.argv)
    if n == 2:
        filename = s.argv[1]
        from_file(filename)
    elif n > 2:
        print("Hiba: Csak egy argumentumot adj meg!")
        return None
    else:
        m = options()
        if m == "2":
            filename = input("Fájlnév: ")
            from_file(filename)
        else:
            data = c.read_user_input()
            c.counting(data)

run()