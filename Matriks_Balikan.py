
import numpy as np

class MatriksBalikan:
    def solve(self):
        print("||Penyelesaian Sistem Persamaan Linier menggunakan Metode Matriks Balikan||")
        print("___________________________________________________________________________")
        
        # Meminta input jumlah variabel
        num_variables = int(input("Masukkan jumlah variabel (2 sampai 4 variabel): "))
        if num_variables < 2 or num_variables > 4:
            print("-- Harap masukkan angka antara 2 sampai 4 --")
            return
        
        # Meminta masukan matriks koefisien dan konstanta dari pengguna
        print("Masukkan matriks koefisien:")
        coefficient_matrix = []
        for i in range(num_variables):
            row = input(f"Masukkan baris ke-{i+1} (pisahkan dengan spasi): ").split()
            # Memastikan jumlah elemen dalam setiap baris sama dengan jumlah variabel
            if len(row) != num_variables:
                print(f"-- Jumlah masukan tidak sesuai dengan jumlah variabel yang dimasukkan ({num_variables}) --")
                return
            coefficient_matrix.append([float(x) for x in row])

        print("Masukkan vektor konstanta:")
        constant_vector = np.array([[float(x)] for x in input("Masukkan elemen vektor konstanta (pisahkan dengan spasi): ").split()])
        
        # Menghitung invers matriks koefisien
        try:
            coefficient_matrix_inv = self.inverse_matrix(coefficient_matrix)
        except np.linalg.LinAlgError:
            print("-- Matriks koefisien tidak memiliki invers. Sistem Error --.")
            return
        
        # Menghitung solusi
        solution_vector = np.dot(coefficient_matrix_inv, constant_vector)
        
        # Menampilkan hasil solusi
        print("\nSolusi:")
        for i in range(num_variables):
            print(f"x{i+1} = {solution_vector[i][0]}")
    
    def inverse_matrix(self, matrix):
        return np.linalg.inv(matrix)

# Banner program
print("|| PROGRAM PENYELESAIAN PERSAMAAN LINIER ||")
print("||   ALMAN KAMAL MAHDI - 21120122120024  ||")
print("||         METODE NUMERIK KELAS B        ||")

print("Silahkan Pilih Metode:")
print("1. Metode Matriks Balikan")
choice = int(input("Masukkan nomor metode yang ingin digunakan: "))

if  choice == 1:
    MatriksBalikan().solve()
else:
    print("-- Pilihan tidak ada. Mohon pilih nomor metode yang tersedia --")
