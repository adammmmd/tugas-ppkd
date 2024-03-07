# Input 90
# Output A
# Jika nilai 90 - 100 maka keluarnya A
# Jika nilai 80 - 89 maka keluarnya B
# Jika nilai 70 - 79 maka keluarnya C
# Jika nilai 60 - 69 maka keluarnya Remedial

# Buatlah function untuk mengklasifikasikan nilai siswa berdasarkan persyaratan diatas menggunakan if elif else
def penilaian_siswa(nilai):
    # Code dibawah sini
    # --------------------------------
    output = ''
    if nilai >= 90:
        output = 'A'
    elif nilai <= 89 and nilai >= 80:
        output = 'B'
    elif nilai <= 79 and nilai >= 70:
        output = 'C'
    else:
        output = 'Remedial'
    
    print(output)
    # --------------------------------

nilai_siswa = 90
penilaian_siswa(nilai_siswa)
nilai_siswa = 89
penilaian_siswa(nilai_siswa)
nilai_siswa = 85
penilaian_siswa(nilai_siswa)
nilai_siswa = 80
penilaian_siswa(nilai_siswa)
nilai_siswa = 79
penilaian_siswa(nilai_siswa)
nilai_siswa = 75
penilaian_siswa(nilai_siswa)
nilai_siswa = 70
penilaian_siswa(nilai_siswa)
nilai_siswa = 69
penilaian_siswa(nilai_siswa)
nilai_siswa = 65
penilaian_siswa(nilai_siswa)
