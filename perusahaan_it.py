# Tugas Python OOP - PerusahaanIT, Karyawan, Mahasiswa

class PerusahaanIT:
    def __init__(self, nama):
        self.nama = nama

class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

class Mahasiswa:
    def __init__(self, nama, kampus):
        self.nama = nama
        self.kampus = kampus

# buat objek
p1 = PerusahaanIT("Nusantara Code")
p2 = PerusahaanIT("Tangerang Tech")

k1 = Karyawan("Budi", "Backend")
m1 = Mahasiswa("Andi", "UNIS")

print(p1.nama)
print(k1.nama, "-", k1.jabatan)
print(m1.nama, "-", m1.kampus)
