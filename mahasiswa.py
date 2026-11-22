# Tugas Python OOP - Class Mahasiswa

class Mahasiswa:
    nim = 0
    nama = ""
    nilai = 0

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

    def hello(self, nama):
        print(f"Halo {nama}, nama saya {self.nama}")

    def grade(self):
        if self.nilai >= 85:
            return "A"
        elif self.nilai >= 75:
            return "B"
        elif self.nilai >= 65:
            return "C"
        elif self.nilai >= 50:
            return "D"
        else:
            return "E"

    def tampil_nilai(self):
        print(f"Nilai {self.nama} (NIM {self.nim}): {self.nilai}, grade {self.grade()}")


# Membuat objek dari class Mahasiswa
mahasiswa = Mahasiswa()
mahasiswa.nama = "Naila"
mahasiswa.nim = 1001
mahasiswa.nilai = 88

# Memanggil method perkenalan, hello, dan tampil_nilai
mahasiswa.perkenalan()
mahasiswa.hello("zakia")
mahasiswa.tampil_nilai()
