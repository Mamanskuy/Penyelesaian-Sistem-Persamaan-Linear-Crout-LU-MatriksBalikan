import numpy as np

class DekomposisiLU:
    def solve(self):
        print("||Penyelesaian Sistem Persamaan Linier menggunakan Metode Dekomposisi LU||")
        print("__________________________________________________________________________")
        
        # Meminta input jumlah variabel
        num_variables = int(input("Masukkan jumlah variabel (2 sampai 4 variabel): "))
        
        # Memastikan input valid
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
        
        # Menghitung solusi
        try:
            solution_vector = self.solve_using_lu(coefficient_matrix, constant_vector)
        except np.linalg.LinAlgError:
            print("Matriks koefisien tidak dapat dipecahkan. Sistem tidak dapat diselesaikan.")
            return
        
        # Menampilkan hasil solusi
        print("\nSolusi:")
        for i in range(num_variables):
            print(f"x{i+1} = {solution_vector[i][0]}")
    
    def solve_using_lu(self, coefficient_matrix, constant_vector):
        # Mendekomposisi matriks koefisien menjadi matriks segitiga atas (U) dan matriks segitiga bawah (L)
        lu_matrix, piv = self.lu_decomposition(coefficient_matrix)
        
        # Menyelesaikan sistem persamaan linier dengan matriks segitiga bawah (L)
        y = self.forward_substitution(lu_matrix, constant_vector, piv)
        
        # Menyelesaikan sistem persamaan linier dengan matriks segitiga atas (U)
        x = self.backward_substitution(lu_matrix, y)
        
        return x
    
    def lu_decomposition(self, matrix):
        n = len(matrix)
        lu_matrix = np.copy(matrix)
        piv = np.arange(n)
        
        for j in range(n-1):
            max_index = np.argmax(abs(lu_matrix[j:, j])) + j
            if max_index != j:
                lu_matrix[[j, max_index]] = lu_matrix[[max_index, j]]
                piv[[j, max_index]] = piv[[max_index, j]]
            
            for i in range(j+1, n):
                lu_matrix[i, j] = lu_matrix[i, j] / lu_matrix[j, j]
                for k in range(j+1, n):
                    lu_matrix[i, k] = lu_matrix[i, k] - lu_matrix[i, j] * lu_matrix[j, k]
                    
        return lu_matrix, piv
    
    def forward_substitution(self, matrix, b, piv):
        n = len(matrix)
        y = np.zeros((n, 1))
        
        for i in range(n):
            y[i] = b[piv[i]]
            for j in range(i):
                y[i] -= matrix[i, j] * y[j]
        
        return y
    
    def backward_substitution(self, matrix, y):
        n = len(matrix)
        x = np.zeros((n, 1))
        
        for i in range(n-1, -1, -1):
            x[i] = y[i]
            for j in range(i+1, n):
                x[i] -= matrix[i, j] * x[j]
            x[i] = x[i] / matrix[i, i]
        
        return x

print("|| PROGRAM PENYELESAIAN PERSAMAAN LINIER ||")
print("||   ALMAN KAMAL MAHDI - 21120122120024  ||")
print("||         METODE NUMERIK KELAS B        ||")
print("Silahkan Pilih Metode:")
print("1. Metode Dekomposisi LU")

choice = int(input("Masukkan nomor metode yang ingin digunakan: "))

if  choice == 1:
    DekomposisiLU().solve()
else:
    print("Pilihan tidak ada. Mohon pilih nomor metode yang tersedia.")
