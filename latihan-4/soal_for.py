# input [1, 2, 3, 4, 5]
# output [1, 4, 9, 16, 25]

# Buatlah function untuk menerima input lalu mengeluarkan output dengan kuadratu
def squares(int_list):
    # Code dibawah sini
    # --------------------------------
    hasil = []
    for i in int_list: hasil.append(i ** 2);
    print(hasil)



    # --------------------------------

list_number = [1, 2, 3, 4, 5]
squares(list_number)
list_number = [2, 3, 4, 5, 6]
squares(list_number)
list_number = [7, 8, 9, 10, 11]
squares(list_number)