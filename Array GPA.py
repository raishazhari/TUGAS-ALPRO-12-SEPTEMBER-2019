def bonus(GPA):
    total = GPA*b
    return total

b = 500000


listGPA = [3, 2.7, 2.5, 4]
for GPA in listGPA:
    if GPA > 3 :
        insentif = bonus(GPA)
        print("Selamat Anda mendapatkan insentif sebesar", "Rp", bonus(GPA))
    else :
        print("Maaf Anda tidak mendapatkan insentif silahkan coba lagi")