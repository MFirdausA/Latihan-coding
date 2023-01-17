print("====PROGRAM INPUT NILAI====")

Nilai=int(input("Masukan Nilai: "))
if Nilai >= 80 and Nilai <100:
    print("Nilai Tugas = A")
elif Nilai >= 70 and Nilai < 80:
    print("Nilai Tugas = B ")
elif Nilai >= 60 and Nilai < 70:
    print("Nilai Tugas = C ")
elif Nilai >= 50 and Nilai < 60:
    print("Nilai Tugas = D ")
else:
    print("Nilai Tugas Kamu Gagal")