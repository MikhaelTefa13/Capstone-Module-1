# Database Karyawan Perusahaan

from tabulate import tabulate
import re
import datetime

data_karyawan = [
    {'ID':'RUDED87', 'Nama':'Rudi Suniardi', 'Birth Date': '10/02/1987','Email':'Rudi.suniardi@gmail.com','Position':'Executive Director', 'Salary':10000000, 'Performance Rating':'A'},
    {'ID':'SAIAM90', 'Nama':'Saiful Riswanto', 'Birth Date': '10/02/1990','Email':'Saifulris90@gmail.com','Position':'Accounting Manager', 'Salary':8000000, 'Performance Rating':'A'},
    {'ID':'RIRCM89', 'Nama':'Ririn Ekawati', 'Birth Date': '10/02/1989','Email':'Ekawarin13@gmail.com','Position':'Communication Manager', 'Salary':8000000, 'Performance Rating':'B'}
]

data_karyawan_bin = [
    {'ID':'MIKCS96', 'Nama':'Mikhael Tefa', 'Birth Date': '01/01/1996','Email':'mikhaelafet@gmail.com','Position':'Creative Specialist', 'Salary':8000000, 'Performance Rating':'C'}
]

# Read Employees Data
def read_data():
    print(tabulate(data_karyawan, headers = 'keys', tablefmt='pretty'))

# Read Employees Data Bin
def read_data_bin():
    print(tabulate(data_karyawan_bin, headers = 'keys', tablefmt='pretty'))

# Main Menu
def main_menu():
    while True:

        print('''
        ####### MOHON MASUKKAN INPUT ANDA! #######

        Pilihan Input
        1. Tampilkan Data Karyawan
        2. Modifikasi Data Karyawan
        3. Exit
        ''')

        opt = input('Pilih input:')
        if opt == '1':
            view_menu()
        elif opt == '2':
            modify_menu()
        elif opt == '3':
            print('Terima kasih, data anda telah kami simpan!')
            exit()
        else:
            print('Input yang anda masukkan salah!')

# View Menu
def view_menu():
    while True:
        read_data()
        print('''
        ####### MOHON MASUKKAN INPUT ANDA! #######

            Pilihan Input
            1. Mengurutkan Data
            2. Lihat Data yang Telah Terhapus
            3. Kembali
            ''')
        
        opt = input('Pilih input')
        if opt == '1':
            sort_data()
        elif opt == '2':
            rest_data()
        elif opt == '3':
            main_menu()
        else:
            print('Input yang anda masukkan salah!')

# Sort Data
def sort_data():
    while True:
        print('''
        ####### MOHON MASUKKAN INPUT ANDA! #######

            Pilihan Input
            1. Urut berdasarkan nama
            2. Urut berdasarkan posisi
            3. Urut berdasarkan salary
            4. Urut berdasarkan performance rating
            5. Kembali
            ''')
        
        opt = input("Pilih input:")
        if opt == '1':
            data_karyawan_sorted = sorted(data_karyawan, key= lambda x: x['Nama'])
            print(tabulate(data_karyawan_sorted, headers = 'keys', tablefmt='pretty'))
        elif opt == '2':
            data_karyawan_sorted = sorted(data_karyawan, key= lambda x: x['Position'])
            print(tabulate(data_karyawan_sorted, headers = 'keys', tablefmt='pretty'))
        elif opt == '3':
            data_karyawan_sorted = sorted(data_karyawan, key= lambda x: x['Salary'])
            print(tabulate(data_karyawan_sorted, headers = 'keys', tablefmt='pretty'))
        elif opt == '4':
            data_karyawan_sorted = sorted(data_karyawan, key= lambda x: x['Performance Rating'])
            print(tabulate(data_karyawan_sorted, headers = 'keys', tablefmt='pretty'))
        elif opt == '5':
            view_menu()
        else:
            print('Input yang anda masukkan salah!')

# Modify Menu
def modify_menu():
    while True:
       
        print('''
        ####### MOHON MASUKKAN INPUT ANDA! #######

        Pilihan Input
        1. Tambahkan Data Karyawan
        2. Hapus Data Karyawan
        3. Rubah Data Karyawan
        4. Lihat Data yang Telah Terhapus
        5. Kembali ke Menu Utama
        6. Exit
        ''')

        opt = input("Pilih input:")
        if opt == '1':
            add_data()
        elif opt == '2':
            del_data()
        elif opt == '3':
            chg_data()
        elif opt == '4':
            rest_data()
        elif opt == '5':
            main_menu()
        elif opt == '6':
            print('Terima kasih, data anda telah kami simpan!')
            exit()
        else:
            print('Input yang anda masukkan salah!')

# Manage Employess Data Bin
def rest_data():
    while True:
        read_data_bin()
        print('''
        ####### MOHON MASUKKAN INPUT ANDA! #######

            Pilihan Input
            1. Pulihkan Data
            2. Format Data
            3. Kembali
            ''')

        opt = input('Pilih input:')
        if opt == '1':
            while True:
                conf = input('Apakah anda yakin? (Y/N)').upper()
                if conf == 'Y':
                    data_karyawan.extend(data_karyawan_bin)
                    data_karyawan_bin.clear()
                    read_data_bin()
                    print('Data berhasil dipulihkan!')
                elif conf == 'N':
                    print('Data tidak dipulihkan.')
                else:
                    print('Input yang anda masukkan salah (Y/N)')
                    continue
                break
        elif opt == '2':
            while True:
                conf = input('Apakah anda yakin? (Y/N)').upper()
                if conf == 'Y':
                    data_karyawan_bin.clear()
                    read_data_bin()
                    print('Data berhasil diformat!')
                elif conf == 'N':
                    print('Data tidak diformat.')
                else:
                    print('Input yang anda masukkan salah (Y/N)')
                    continue
                break
        elif opt == '3':
            main_menu()
        else:
            print('Input yang anda masukkan salah!')

# Name Input Verification
def input_nam():
    while True:
        nama = input('Masukkan nama karyawan: ')
        if nama.replace(' ','').isalpha():
            return nama.title()
        else:
            print('Harap hanya memasukan nama (tanpa simbol dan angka)')

# Birth Date Verification
def input_date():
    while True:
        try:
            date = input('Masukkan tanggal lahir (format DD/MM/YYYY): ')
            birthdate = datetime.datetime.strptime(date,'%d/%m/%Y').date()
            return birthdate
        except ValueError:
            print('Format yang anda masukkan salah, harap gunakan format DD/MM/YYYY')

# Email Verification            
def input_em():
    while True:
        email = input('Masukkan email karyawan: ')
        match = re.search(r'\b\w+(?:\.?\w?)*\@\w+(?:\.?\w?)*\.\w{2,}\b', email)
        if match:
            return email
        else:
            print('Masukkan format email yang benar!')

# Postition Input Verification
def input_pos():
    while True:
        position = input('Masukkan posisi karyawan: ')
        if position.replace(' ','').isalpha():
            return position.title()
        else:
            print('Harap hanya memasukan posisi (tanpa simbol dan angka)')

# Salary Verification
def input_sal():
    while True:
        try:
            salary = int(input('Masukkan gaji: '))
            return salary
        except ValueError:
            print('Harap masukkan input dalam bentuk angka.')

# Performance Verification
def input_per():
    while True:
        rating = ['A', 'B', 'C', 'D', 'E']
        perform = input('Masukkan performance rating karyawan (skala A-E): ').upper()
        match = re.search(r'\b[a-zA-Z]\b', perform)
        if match and perform in rating:
            return perform
        else:
            print('Salah format! Harap masukkan berdasarkan skala A-E)')

# Add Data Function
def add_data():
    nama = input_nam()
    nama_short = nama[0:3].upper()
    birth_date = input_date().strftime('%d/%m/%Y')
    year_short = birth_date[-2:]
    email = input_em()
    position = input_pos()
    position_initial = ''.join(i[0] for i in position.split())
    salary = input_sal()
    performance_rating = input_per()
    id = ''.join([nama_short, position_initial, year_short])
    data_karyawan.append({'ID':id, 'Nama':nama, 'Birth Date':birth_date, 'Email':email, 'Position':position, 'Salary':salary, 'Performance Rating': performance_rating})
    read_data()
    print('Data karyawan berhasil ditambahkan')

# Delete Data Function
def del_data():
    read_data()
    while True:
        iden = input('Masukkan ID Karyawan yang ingin anda hapus: ').upper()
        found = False
        for i in data_karyawan:
            if i['ID'] == iden:
                print(i)
                conf = input('Apakah ini data yang ingin anda hapus? (Y/N): ').upper()
                if conf == 'Y':
                    data_karyawan_bin.append(i)
                    data_karyawan.remove(i)
                    read_data()
                    print('Data berhasil dihapus.')
                elif conf == 'N':
                    print('Data tidak dihapus.')
                else:
                    print('Input yang anda masukkan salah (Y/N)')
                found = True
                break
        if not found:
            print('ID tidak ditemukan, periksa kembali ID Karyawan yang anda masukkan!')

        ulang = input('Apakah ingin melanjutkan penghapusan? (Y/N): ').upper()
        if ulang == 'N':
            return
        elif ulang != 'Y':
            print('Input yang anda masukkan salah (Y/N)')

# Change Data Function
def chg_data():
    read_data()
    while True:
        iden = input('Masukkan ID Karyawan yang ingin anda rubah: ').upper()
        found = False
        for i in data_karyawan:
            if i['ID'] == iden:
                print(i)
                while True:
                    opt = input('Pilih data yang ingin anda rubah: ').title()
                    if opt == 'Nama':
                        found = True
                        i['Nama'] = input_nam()
                    elif opt == 'Birth Date':
                        found = True
                        i['Birth Date'] = input_date().strftime('%d/%m/%Y')
                    elif opt == 'Email':
                        found = True
                        i['Email'] = input_em()
                    elif opt == 'Position':
                        found = True
                        i['Position'] = input('Masukkan posisi: ').title()
                    elif opt == 'Salary':
                        found = True
                        i['Salary'] = input_sal()
                    elif opt == 'Performance Rating':
                        found = True
                        i['Performance Rating'] = input_per()
                    else:
                        print('Input yang anda masukkan salah! Harap coba kembali')
                        continue
                    break
                break
        if not found:
            print('ID yang anda masukkan tidak ditemukan! Harap coba kembali!')
        else:
            print(i)
            print('Data anda berhasil dirubah')
            ulang = input('Apakah ingin melanjutkan perubahan data karyawan? (Y/N): ').upper()
            if ulang == 'N':
                return
            elif ulang != 'Y':
                print('Input yang anda masukkan salah (Y/N)')

main_menu()