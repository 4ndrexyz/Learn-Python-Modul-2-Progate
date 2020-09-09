# Menyusun Data

# Ketika ada daftar nama-nama makanan, sebagai contoh, tidak efisien untuk menamainya dengan variable terpisah, seperti food1, food2, food3. 
# Akan lebih baik untuk mempunyai variable foods untuk mengelola keseluruhan daftar tersebut.
# Variable adalah mengelola data secara mandiri.
# List adalah mengelola sekelompok data secara bersamaan

# ---------------------------------

# List (Daftar)

#Tipe data list memungkinkan Anda untuk mengelola sekelompok data sekaligus. 
# Anda dapat membuat list sebagai berikut: [element1, element2, ...]. Setiap nilai di dalam list disebut element.
# Dengan menggunakan list, Anda dapat mengelola banyak string dan integer dalam satu grup.

[element1, elemet2, element3]   # pisahkan element dengan koma (,) 

# List dari beberapa string
['pasta', 'gulai', 'sushi']

# List dari beberapa integer
[1, 2, 3,5, 8, 13, 21]

# List dari item gabungan
['apel', 'pisang', 200, 300]

# ---------------------------------

# Menetapkan List ke Variable

# Seperti integer dan string, Anda dapat menentukan list ke dalam satu variable. 
# Sesuai norma penamaan yang berlaku, nama variable bersifat plural, seperti foods, karena variable akan mengandung banyak element.

foods = ['pasta', 'gulai', 'sushi']
print(foods)
# output = ['pasta', 'gulai', 'sushi']   <- list dicetak sebagaimana adanya

# ---------------------------------

# Menentukan Element dalam List

# Setiap element list dinomori 0, 1, 2, ....
# Ini disebut nomor indeks. Nomor indeks dimulai dari 0. 
# Anda bisa mendapatkan element individual dengan menulis list[index].

foods = ['pasta', 'gulai', 'sushi']
print('Saya suka ' + foods[2])  # (foods[2]) mengambil element menggunakan nomor index
# output = Saya suka sushi   # element dengan index 2 di cetak
