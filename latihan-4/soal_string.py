# input nama_depan = stephen
# input nama_belakang = leonardo
# output Stephen Leonardo

# Buatlah function untuk menerima nama depan dan nama belakang lalu mengeluarkan output nama_lengkap dengan huruf kapital di huruf awal
def nama_lengkap(nama_depan, nama_belakang):
    # Code dibawah sini
    # --------------------------------
    print(f'{nama_depan.capitalize()} {nama_belakang.capitalize()}')

    # --------------------------------

nama_depan = "stephen"
nama_belakang = "leonardo"
nama_lengkap(nama_depan, nama_belakang)
nama_depan_1 = "justin"
nama_belakang_1 = "clooney"
nama_lengkap(nama_depan_1, nama_belakang_1)