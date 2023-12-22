import exceptions as e

# counts
def counting(data: list) -> None:
    if data == []:
        print("Hiba: Üres lista (counting)")
        return None
    
    multipled = 0
    credit_sum = 0
    credit_ok = 0
    grade_sum = 0
    n = 0

    for (c, g) in data:
        n += 1
        credit_sum += c
        grade_sum += g
        if g > 1:
            multipled += (c * g)
            credit_ok += c
    
    sum_per_ok = credit_ok / float(credit_sum)
    ki = float(multipled) / 30
    kki = ki * sum_per_ok
    ha_avg = float(grade_sum) / n
    ta = float(multipled) / credit_ok

    print("\nEredmények\n")
    print("Kreditindex (KI):", round(ki, 2))
    print("Korrigált kreditindex (KKI):", round(kki, 2))
    print("Teljesített kredit:", credit_ok)
    print("Hagyományos átlag:", round(ha_avg, 2))
    print("Súlyozott átlag (TÁ):", round(ta, 2))

    with open("results/your_results.txt", "w", encoding="utf8") as file:
        file.write("Eredmények\n")
        file.write(f"Kreditindex (KI): {round(ki, 2)}\n")
        file.write(f"Korrigált kreditindex (KKI): {round(kki, 2)}\n")
        file.write(f"Teljesített kredit: {credit_ok}\n")
        file.write(f"Hagyományos átlag: {round(ha_avg, 2)}\n")
        file.write(f"Súlyozott átlag (TÁ): {round(ta, 2)}")

# get input
def read_from_file(filename: str) -> list:
    data = []

    if filename.endswith(".txt"):
        filename = filename.replace(".txt", "")
    filename = "grades/" + filename + ".txt"

    try:
        with open(filename, "r", encoding="utf8") as file:
            input = file.read().split('\n')
            for i in input:
                if (i.strip()):
                    tmp = i.split(';')

                    if (len(tmp) < 3):
                        raise e.EmptyCreditOrGradeException

                    if (not tmp[1].strip() or not tmp[2].strip()):
                        raise e.EmptyCreditOrGradeException
                    
                    credit = int(tmp[1])
                    grade = int(tmp[2])

                    if credit < 0 or (grade < 1 and grade > 5):
                        raise ValueError
                    
                    data.append((credit, grade))
    except FileNotFoundError:
        print("Hiba: A megadott fájl nem található (read_from_file)")
    except ValueError:
        print("Hiba: Hibás kredit szám vagy jegy érték (read_from_file)")
    except e.EmptyCreditOrGradeException:
        print("Hiba: Hiányzó kredit vagy jegy (read_from_file)")
        print("Ellenőrizd, hogy beírtad-e az összes jegyet és kreditet!")
    except:
        print("Hiba: Egyéb hiba (read_from_file)")
    return data

def read_user_input() -> list:
    data = []
    print("Új tárgyhoz: +")
    m = input("Új tárgy: ")
    while m == "+":
        try:
            credit = int(input("Kredit: "))
            if credit < 0:
                raise ValueError
            grade = int(input("Jegy: "))
            if grade < 1 or grade > 5:
                raise ValueError
        except ValueError:
            print("Helytelen adat\nÚj tárgy")
            continue
        data.append((credit, grade))
        m = input("Új tárgy: ")    
    return data

# doc format
def check_format(filename: str) -> bool:
    if filename.endswith(".txt"):
        filename = filename.replace(".txt", "")
    filename = "grades/" + filename + ".txt"

    try:
        with open(filename, "r", encoding="utf8") as file:
            input = file.read().split('\n')
            for i in input:
                if (i.strip()):
                    tmp = i.split(';')
                    if (len(tmp) < 3):
                        raise e.EmptyCreditOrGradeException
    except FileNotFoundError:
        print("Hiba: A megadott fájl nem található (check_format)")
        return False
    except e.EmptyCreditOrGradeException:
        print("Hiba: fomátum hiba (check_format)")
        return False
    except:
        print("Hiba: fomátum hiba (check_format)")
        return False    
    return True

def modify(filename: str):
    content = []
    filename = "grades/" + filename + ".txt"
    with open(filename, "r", encoding="utf8") as file:
        input = file.read().split('\n')
        for r in input:
            if (r.strip()):
                r = r.rstrip()
                r = r.replace('\t', ';')
                tmp = r.split(';')[1:3] + [""]
                r = ';'.join(tmp)
                content.append(r)
    
    with open(filename, "w", encoding="utf8") as file:
        file.write('\n'.join(content))
