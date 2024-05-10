import numpy as np

class DekomposisiCrout:
    def solve(self):
        print("Penyelesaian Sistem Persamaan Linier menggunakan Metode Crout")
        print("_____________________________________________________________")
        
        # Meminta input jumlah variabel
        num_variables = int(input("Masukkan jumlah variabel (2 sampai 4): "))
        
        # Memastikan input valid
        if num_variables < 2 or num_variables > 4:
            print("Harap masukkan angka antara 2 sampai 4.")
            return
        
        # Meminta masukan matriks koefisien dan konstanta dari pengguna
        print("Masukkan matriks koefisien:")
        coefficient_matrix = []
        for i in range(num_variables):
            row = input(f"Masukkan baris ke-{i+1} (pisahkan elemen dengan spasi): ").split()
            if len(row) != num_variables:
                print(f"Jumlah elemen tidak sesuai dengan jumlah variabel yang dimasukkan ({num_variables})")
                return
            coefficient_matrix.append([float(x) for x in row])
        print("Masukkan vektor konstanta:")
        constant_vector = np.array([[float(x)] for x in input("Masukkan elemen vektor konstanta (pisahkan dengan spasi): ").split()])

        try:
            # Menyelesaikan sistem persamaan linier menggunakan metode Crout
            solution = self.solve_with_crout(coefficient_matrix, constant_vector)
            # Menampilkan hasil
            print("\nSolusi:")
            for i in range(num_variables):
                print(f"x{i+1} = {solution[i][0]}")
        except np.linalg.LinAlgError:
            print("Matriks koefisien tidak dapat dipecahkan. Sistem tidak dapat diselesaikan.")
            return

    # Fungsi untuk melakukan dekomposisi Crout
    def crout_decomposition(self, A):
        n = len(A)
        L = np.zeros((n, n))
        U = np.zeros((n, n))
        
        for j in range(n):
            U[j][j] = 1
            
            for i in range(j, n):
                L[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
                
            for i in range(j+1, n):
                U[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(j))) / L[j][j]
        
        return L, U

    # Fungsi untuk mencari solusi dengan dekomposisi Crout
    def solve_with_crout(self, A, b):
        L, U = self.crout_decomposition(A)
        
        # Menyelesaikan Ly = b
        y = np.linalg.solve(L, b)
        
        # Menyelesaikan Ux = y
        x = np.linalg.solve(U, y)
        
        return x

print("|| PROGRAM PENYELESAIAN PERSAMAAN LINIER ||")
print("||   ALMAN KAMAL MAHDI - 21120122120024  ||")
print("||         METODE NUMERIK KELAS B        ||")
print("Silahkan Pilih Metode:")
print("1. Metode Dekomposisi Crout")

choice = int(input("Masukkan nomor metode yang ingin digunakan: "))

if  choice == 1:
    DekomposisiCrout().solve()
else:
    print("Pilihan tidak ada. Mohon pilih nomor metode yang tersedia.")
