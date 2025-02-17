# List berisi data koleksi dalam bentuk dictionary
data_collection = [
    {"Collection ID": "F01", "Title": "Tyrannosaurus Rex Fossil's", "Region of Origin": "North America", "Place Discovered": "Dakota, United States of America", "Era": "Cretaceous", "Year Discovered": 1990, "Type": "Fossil", "Status": "Displayed"},
    {"Collection ID": "F02", "Title": "Mammoth Tusk", "Region of Origin": "Eurasia", "Place Discovered": "Siberia, Russia", "Era": "Pleistocene", "Year Discovered": 2003, "Type": "Fossil", "Status": "Restoration"},
    {"Collection ID": "F03", "Title": "Trilobite Fossil", "Region of Origin": "Africa", "Place Discovered": "Morocco", "Era": "Cambrian", "Year Discovered": 1995, "Type": "Fossil", "Status": "Displayed"},
    {"Collection ID": "F04", "Title": "Ichthyosaur Skeleton", "Region of Origin": "Europe", "Place Discovered": "Holzmaden, Germany", "Era": "Jurassic", "Year Discovered": 1890, "Type": "Fossil", "Status": "Displayed"},
    {"Collection ID": "F05", "Title": "Megatherium Claw", "Region of Origin": "South America", "Place Discovered": "Argentina", "Era": "Pleistocene", "Year Discovered": 1788, "Type": "Fossil", "Status": "Storaged"},
    {"Collection ID": "W01", "Title": "Oda Nobunaga Katana's: Heshikiri Hasebe", "Region of Origin": "Japan", "Place Discovered": "Kyoto, Japan", "Era": "Sengoku Period", "Year Discovered": 1987, "Type": "Weapon", "Status": "Storaged"},
    {"Collection ID": "W02", "Title": "Napoleon Bonaparte's Saber", "Region of Origin": "Europe", "Place Discovered": "Paris, France", "Era": "Napoleonic Wars", "Year Discovered": 1815, "Type": "Weapon", "Status": "Displayed"},
    {"Collection ID": "W03", "Title": "Viking Battle Axe", "Region of Origin": "Scandinavia", "Place Discovered": "Norway", "Era": "Viking Age", "Year Discovered": 1972, "Type": "Weapon", "Status": "Displayed"},
    {"Collection ID": "W04", "Title": "Roman Gladius", "Region of Origin": "Europe", "Place Discovered": "Pompeii, Italy", "Era": "Roman Republic", "Year Discovered": 1875, "Type": "Weapon", "Status": "Displayed"},
    {"Collection ID": "W05", "Title": "Samurai Armor", "Region of Origin": "Japan", "Place Discovered": "Osaka, Japan", "Era": "Edo Period", "Year Discovered": 1923, "Type": "Weapon", "Status": "Storaged"},
    {"Collection ID": "A01", "Title": "Venus of Willendorf", "Region of Origin": "Europe", "Place Discovered": "Willendorf, Austria", "Era": "Paleolithic", "Year Discovered": 1908, "Type": "Artifact", "Status": "Displayed"},
    {"Collection ID": "A02", "Title": "Rosetta Stone", "Region of Origin": "Africa", "Place Discovered": "El-Rashid (Rosetta), Egypt", "Era": "Ptolemaic Period", "Year Discovered": 1799, "Type": "Artifact", "Status": "Displayed"},
    {"Collection ID": "A03", "Title": "Terracotta Warrior", "Region of Origin": "China", "Place Discovered": "Xi'an, China", "Era": "Qin Dynasty", "Year Discovered": 1974, "Type": "Artifact", "Status": "Displayed"},
    {"Collection ID": "A04", "Title": "Mayan Calendar Stone", "Region of Origin": "Mesoamerica", "Place Discovered": "Mexico City, Mexico", "Era": "Postclassic Period", "Year Discovered": 1790, "Type": "Artifact", "Status": "Displayed"},
    {"Collection ID": "A05", "Title": "Sumerian Cuneiform Tablet", "Region of Origin": "Middle East", "Place Discovered": "Iraq", "Era": "Bronze Age", "Year Discovered": 1929, "Type": "Artifact", "Status": "Storaged"},
    {"Collection ID": "P01", "Title": "Mona Lisa", "Region of Origin": "Europe", "Place Discovered": "Florence, Italy", "Era": "Renaissance", "Year Discovered": 1517, "Type": "Painting", "Status": "Displayed"},
    {"Collection ID": "P02", "Title": "The Starry Night", "Region of Origin": "Europe", "Place Discovered": "Saint-Rémy-de-Provence, France", "Era": "Post-Impressionism", "Year Discovered": 1889, "Type": "Painting", "Status": "Displayed"},
    {"Collection ID": "P03", "Title": "The Great Wave off Kanagawa", "Region of Origin": "Japan", "Place Discovered": "Japan", "Era": "Edo Period", "Year Discovered": 1831, "Type": "Painting", "Status": "Displayed"},
    {"Collection ID": "P04", "Title": "Guernica", "Region of Origin": "Europe", "Place Discovered": "Madrid, Spain", "Era": "Modern Art", "Year Discovered": 1937, "Type": "Painting", "Status": "Displayed"},
    {"Collection ID": "P05", "Title": "The Last Supper", "Region of Origin": "Europe", "Place Discovered": "Milan, Italy", "Era": "Renaissance", "Year Discovered": 1498, "Type": "Painting", "Status": "Displayed"}
]

# Membuat set kosong untuk menyimpan ID yang sudah digunakan
used_ids = set()

# Mengimpor library 'tabulate' untuk mencetak tabel secara rapi
from tabulate import tabulate

# Fungsi untuk menampilkan salam pembuka
def greeting () :
    print("""
          Welcome to Shangri-La Museum Application
          """)

# Fungsi untuk menampilkan menu utama
def main_menu () :

    # Loop agar menu terus muncul sampai user memilih keluar
    while True :
        
        # Menampilkan pilihan menu
        print("""
        Menu :
              1. Show Collection
              2. Add Collection
              3. Update Collection
              4. Delete Collection
              5. Exit Program
              """)
        try : # Menangkap error jika input bukan angka
            menu_input = int(input("Input Menu That You Want to Run : ").strip()) # Membaca input menu dan menghapus spasi
            if menu_input == 1 : # Jika user pilih 1, jalankan fungsi read_menu ()
                read_menu ()
            elif menu_input == 2 : # Jika user pilih 2, jalankan fungsi create_menu ()
                create_menu ()
            elif menu_input == 3 : # Jika user pilih 3, jalankan fungsi update_menu ()
                update_menu ()
            elif menu_input == 4 : # Jika user pilih 4, jalankan fungsi delete_menu()
                delete_menu()
            elif menu_input == 5 : # Jika user pilih 5, keluar dari loop dan program selesai
                print("""
        Thank You for Using Our Service!
        Exit Program...
                      """)
                break
            else : # Jika input di luar 1-5
                print("The Option You Entered is Not Valid! Please Choose Between 1-5.")
                continue
        except ValueError : 
            print("The Option You Entered is Not Valid! Please Enter a Number.")

# Fungsi untuk menampilkan submenu 'Read Data'
def read_menu () :
    while True :
        print("""
        Read Data Menu :
            1. Show All Collections
            2. Search by Collection ID
            3. Search by Other Attributes
            4. Back to Main Menu
        """)

        menu_input = input("Input Menu That You Want to Run : ").strip()

        if menu_input == "1" : # Menampilkan semua koleksi
            if not data_collection : # Cek jika koleksi kosong
                print("No Collections Available.")
            else:
                read_data_collection () # Tampilkan semua koleksi
        
        elif menu_input == "2" : # Cari berdasarkan ID koleksi
            if not data_collection:
                print("No Collections Available.")
            else:
                collection_id = input("Enter Collection ID: ").strip()
                read_data_collection("Collection ID", collection_id)
        
        elif menu_input == "3" : # Cari berdasarkan value key yang lain
            if not data_collection:
                print("No Collections Available.")
            else:
                search_by_attribute()
        
        elif menu_input == "4" : # Kembali ke menu utama
            print("Returning to Main Menu...")
            break
        
        else:
            print("The Option You Entered is Not Valid! Please Choose Between 1-4.")

# Fungsi membaca data dengan atau tanpa filter
def read_data_collection (filter_option=None, filter_value=None) :
    if not data_collection : # Jika data_collection kosong, tampilkan pesan dan keluar dari fungsi
        print("No Collections Available.")
        return
    
    filtered_data = [] # List kosong untuk menyimpan data yang sesuai dengan filter

    for i in range(len(data_collection)) : # Loop melalui setiap item dalam data_collection
        item = data_collection[i] # Mengakses elemen saat ini dalam loop

        # Jika ada filter yang diberikan, lakukan pencocokan data
        if filter_option and filter_value :
            if filter_option == "Collection ID" : # Filter berdasarkan Collection ID (harus sama persis)
                if str(item["Collection ID"]) != filter_value :
                    continue # Lewati iterasi jika tidak cocok
            elif filter_option == "Title" :
                if filter_value not in item["Title"] : # Filter berdasarkan Title (cocok sebagian)
                    continue
            elif filter_option == "Region of Origin" :
                if filter_value not in item["Region of Origin"] : # Filter berdasarkan Region of Origin
                    continue
            elif filter_option == "Place Discovered" :
                if filter_value not in item["Place Discovered"] : # Filter berdasarkan Place Discovered
                    continue
            elif filter_option == "Era" :
                if filter_value not in item["Era"] : # Filter berdasarkan Era
                    continue
            elif filter_option == "Type" :
                if filter_value not in item["Type"] : # Filter berdasarkan Type
                    continue
            elif filter_option == "Status" :
                if filter_value not in item["Status"] : # Filter berdasarkan Status
                    continue
            elif filter_option == "Year Discovered" : # Filter berdasarkan Year Discovered
                try :
                    if int(item["Year Discovered"]) != int(filter_value) : # Bandingkan sebagai angka
                        continue
                except ValueError : # Tangani kesalahan jika input bukan angka
                    print("Invalid Year Format! Please Enter a Number.")
                    return
        
        filtered_data.append(item) # Jika lolos filter, tambahkan ke filtered_data

    if not filtered_data : # Jika tidak ada data yang cocok, tampilkan pesan
        print("No Matching Data Found.")
    else :
        headers = filtered_data[0].keys() # Ambil nama kolom dari item pertama
        rows = [item.values() for item in filtered_data] # Ambil nilai dari setiap item
        print("\nCollection List")
        print(tabulate(rows, headers=headers, tablefmt="rst")) # Tampilkan dalam format tabel

# Fungsi untuk mencari koleksi berdasarkan atribut tertentu
def search_by_attribute () :
    while True : # Loop agar pengguna dapat mencoba lagi jika input salah
        filter_key = input("Enter The Attribute to Filter by : ").strip() # Menerima input nama atribut

        # Jika atribut yang dimasukkan adalah "Year Discovered", validasi sebagai angka
        if filter_key == "Year Discovered":
            try:
                filter_value = int(input("Enter Year Discovered to search (Numbers Only) : ").strip())
                read_data_collection("Year Discovered", str(filter_value)) # Panggil fungsi baca data dengan filter
                break # Keluar dari loop jika input valid
            except ValueError :
                print("Invalid Year Format! Please Enter a Number.") # Tampilkan pesan error jika input bukan angka

        # Jika atribut yang dimasukkan adalah "Title", lakukan pencarian berdasarkan judul
        elif filter_key == "Title" :
            filter_value = input("Enter Title to Search: ").strip()
            read_data_collection("Title", filter_value)
            break
        
        # Jika atribut yang dimasukkan adalah "Region of Origin", lakukan pencarian berdasarkan wilayah asal
        elif filter_key == "Region of Origin" :
            filter_value = input("Enter Region of Origin to Search : ").strip()
            read_data_collection("Region of Origin", filter_value)
            break
        
        # Jika atribut yang dimasukkan adalah "Place Discovered", lakukan pencarian berdasarkan tempat ditemukan
        elif filter_key == "Place Discovered" :
            filter_value = input("Enter Place Discovered to Search : ").strip()
            read_data_collection("Place Discovered", filter_value)
            break
        
        # Jika atribut yang dimasukkan adalah "Era", lakukan pencarian berdasarkan era
        elif filter_key == "Era" :
            filter_value = input("Enter Era to Search : ").strip()
            read_data_collection("Era", filter_value)
            break
        
        # Jika atribut yang dimasukkan adalah "Type", lakukan pencarian berdasarkan tipe koleksi
        elif filter_key == "Type" :
            filter_value = input("Enter Type to Search : ").strip()
            read_data_collection("Type", filter_value)
            break
        
        # Jika atribut yang dimasukkan adalah "Status", lakukan pencarian berdasarkan status koleksi
        elif filter_key == "Status" :
            filter_value = input("Enter Status to Search : ").strip()
            read_data_collection("Status", filter_value)
            break
        
        # Jika atribut yang dimasukkan tidak valid, tampilkan pesan error dan daftar atribut yang benar
        else:
            print("The Attribute You Entered is Not Valid! Please Enter a Valid Attribute.")
            print("Valid Attributes : Title, Region of Origin, Place Discovered, Era, Year Discovered, Type, Status.")

# Fungsi untuk menampilkan submenu 'Create Data'
def create_menu () :
    while True :
        print("""
        Create Data Menu:
            1. Add New Collection
            2. Back to Main Menu
        """)
        menu_input = input("Input Menu That You Want to Run : ").strip()

        if menu_input == "1" : # Panggil fungsi tambah data
            create_data_collection ()
        elif menu_input == "2" : # Kembali ke menu utama
            print("Returning to Main Menu...")
            break
        else:
            print("The Option You Entered is Not Valid! Please Choose Between 1 or 2.")

# Fungsi create_data_collection digunakan untuk menambahkan koleksi baru ke data_collection
def create_data_collection () :
    
    # Menggunakan variabel global used_ids untuk melacak ID yang sudah digunakan
    global used_ids

    while True :
        # Meminta input Collection ID
        data_id = input("Input Collection ID : ").strip()
        if not data_id : 
            # Jika input kosong, tampilkan pesan dan ulangi
            print("Collection ID Cannot be Empty.")
            continue

        duplicate = False # Untuk cek duplikasi
        for i in range(len(data_collection)) : # Iterasi untuk cek setiap data
            if data_collection[i]["Collection ID"] == data_id :
                duplicate = True # Tandai jika ID sudah ada
                break
        
        if data_id in used_ids : # Jika ID ada di set used_ids
            print("Collection ID has Already Been Used! Please Enter a New Collection ID.")
            continue

        if duplicate :
            print("Collection ID Already Exists! Please Enter a Different ID.")
            continue
        else: 
            break # Keluar dari loop jika ID valid
    
    # Meminta input detail koleksi lainnya
    data_title = input("Input Data Title : ").strip()
    data_origin = input("Input Data Region of Origin : ").strip()
    data_place = input("Input Data Place Discovered : ").strip()
    data_era = input("Input Data Era : ").strip()

    while True :
        try:
            data_year = int(input("Input Data Year : ").strip())
            if 0 <= data_year <= 2025 : # Validasi tahun
                break
            else :
                print("Year Discovered Must be Between 0 and 2025.")
        except ValueError : # Tangani error jika input bukan angka
            print("Invalid Year Format! Please Enter a Number.")

    data_type = input("Input Data Type : ").strip()
    data_status = input("Input Data Status : ").strip()
    
    # Cek jika ada input kosong
    if not data_id.strip() or not data_title.strip() or not data_origin.strip() or not data_place.strip() or not data_era.strip() or not data_year.strip() or not data_type.strip() or not data_status.strip() :
        print("Invalid Input! Please Enter All Data Details.")
        return

    # Menampilkan data yang telah diinput untuk dikonfirmasi
    print("\nPlease Review The Entered Data :")
    print(f"Collection ID : {data_id}")
    print(f"Title : {data_title}")
    print(f"Region of Origin : {data_origin}")
    print(f"Place Discovered : {data_place}")
    print(f"Era : {data_era}")
    print(f"Year Discovered : {data_year}")
    print(f"Type : {data_type}")
    print(f"Status : {data_status}")

    # Membuat dictionary baru dengan data yang diinput
    new_data = {
        "Collection ID" : data_id,
        "Title" : data_title,
        "Region of Origin" : data_origin,
        "Place Discovered" : data_place,
        "Era" : data_era,
        "Year Discovered" : data_year,
        "Type" : data_type,
        "Status" : data_status
    }
    print(tabulate([new_data.values()], headers=new_data.keys(), tablefmt="rst"))

    while True :
        # Konfirmasi penyimpanan data
        confirm = input("Do You Want to Save the Data? (Yes/No): ").strip().lower()
        if confirm == "yes":
            data_collection.append({
                "Collection ID" : data_id,
                "Title" : data_title,
                "Region of Origin" : data_origin,
                "Place Discovered" : data_place,
                "Era" : data_era,
                "Year Discovered" : data_year,
                "Type" : data_type,
                "Status" : data_status
                }) # Menambahkan data ke koleksi
            used_ids.add(data_id) # Menambahkan ID ke set used_ids
            print("Data Successfully Saved! Returning to Create Data Menu...")
            return
        elif confirm == "no":
            print("Data Entry Canceled. Returning to Create Data Menu...")
            return
        else:
            print("Invalid Input! Please enter 'Yes' or 'No'.") # Pesan error jika input invalid

# Fungsi untuk menampilkan submenu 'Update Data'
def update_menu () :
    while True:
        print("""
        Update Data Menu :
            1. Update a Collection by Collection ID
            2. Back to Main Menu
        """)
        
        menu_input = input("Input Menu That You Want to Run : ").strip()

        if menu_input == "1" : # Panggil fungsi update data
            update_data_collection ()
        elif menu_input == "2" : # Kembali ke menu utama
            print("Returning to Main Menu...")
            break
        else:
            print("The Option You Entered is Not Valid! Please Choose Between 1 or 2.")

# Fungsi untuk mengupdate data koleksi
# Menampilkan data berdasarkan Collection ID yang dimasukkan, lalu meminta input kolom yang ingin diupdate dan nilai barunya
def update_data_collection() :
    # Jika data_collection kosong, tampilkan pesan dan keluar
    if not data_collection :
        print("No Collections Available.")
        return

    # Meminta input Collection ID untuk data yang ingin diupdate
    update_id = input("Input Collection ID of The Item You Want to Update : ").strip()

    # Validasi jika input kosong
    if not update_id :
        print("Collection ID Cannot Be Empty.")
        return

    # Mencari data dengan Collection ID yang sesuai
    collection_to_update = None
    for item in data_collection :
        if item["Collection ID"] == update_id :
            # Menampilkan data yang ditemukan dalam bentuk tabel
            print("\nCurrent Data:")
            print(tabulate([item.values()], headers=item.keys(), tablefmt="rst"))
            collection_to_update = item
            break
    
    # Jika tidak ditemukan, tampilkan pesan
    if not collection_to_update :
        print("The Data You are Looking for Does Not Exist!")
        return

    # Menampilkan data yang akan diupdate
    print("\nPlease Review The Selected Data :")
    for key, value in collection_to_update.items() :
        print(f"{key}: {value}")

    # Memastikan pengguna ingin melanjutkan update
    while True :
        confirm = input("Continue Update? (Yes/No) : ").strip().lower()
        if confirm == "yes" :
            break
        elif confirm == "no" :
            print("Update Canceled. Returning to Update Data Menu...")
            return
        else:
            print("Invalid Input! Please enter 'Yes' or 'No'.")

    # Daftar kolom yang valid dan nama asli kolom untuk memudahkan pencocokan
    valid_columns = ["title", "region of origin", "place discovered", "era", "year discovered", "type", "status"]
    original_columns = ["Title", "Region of Origin", "Place Discovered", "Era", "Year Discovered", "Type", "Status"]

    # Loop untuk meminta kolom yang ingin diupdate
    while True :
        print("Valid columns to update : Title, Region of Origin, Place Discovered, Era, Year Discovered, Type, Status")
        column_to_update = input("Enter The Column You Want to Update : ").strip().lower()

        # Validasi kolom input
        if column_to_update not in valid_columns :
            print("Invalid Input! Please Enter a Valid Column.")
            continue
        
        # Mendapatkan nama kolom asli berdasarkan indeks
        column_index = valid_columns.index(column_to_update)
        column_name = original_columns[column_index]

        # Meminta input nilai baru berdasarkan kolom yang dipilih
        if column_name == "Title" :
            new_value = input("Enter New Value for Title : ").strip()
            if not new_value :
                print("Invalid Input! New Value Cannot be Empty.")
                continue
        elif column_name == "Region of Origin" :
            new_value = input("Enter New Value for Region of Origin : ").strip()
            if not new_value:
                print("Invalid Input! New Value Cannot be Empty.")
                continue
        elif column_name == "Place Discovered" :
            new_value = input("Enter New Value for Place Discovered : ").strip()
            if not new_value:
                print("Invalid Input! New Value Cannot be Empty.")
                continue
        elif column_name == "Era" :
            new_value = input("Enter New Value for Era : ").strip()
            if not new_value:
                print("Invalid Input! New Value Cannot be Empty.")
                continue
        elif column_name == "Year Discovered" :
            while True :
                try :
                    new_value = int(input("Enter New Value for Year Discovered (Numbers Only) : ").strip())
                    if 0 <= new_value <= 2025 :
                        break
                    else :
                        print("Year Discovered Must be Between 0 and 2025.")
                except ValueError :
                    print("Invalid Year Format! Please Enter a Number.")
        elif column_name == "Type" :
            new_value = input("Enter New Value for Type : ").strip()
            if not new_value :
                print("Invalid Input! New Value Cannot be Empty.")
                continue
        elif column_name == "Status" :
            new_value = input("Enter New Value for Status : ").strip()
            if not new_value :
                print("Invalid Input! New Value Cannot be Empty.")
                continue
        
        # Konfirmasi update dari pengguna
        while True :
            confirm_update = input("Do You Want to Update the Data? (Yes/No) : ").strip().lower()
            if confirm_update == "yes" :
                collection_to_update[column_name] = new_value
                print(tabulate([collection_to_update.values()], headers=collection_to_update.keys(), tablefmt="rst"))
                print("Data Successfully Updated! Returning to Update Data Menu...")
                return
            elif confirm_update == "no" :
                print("Update Canceled. Returning to Update Data Menu...")
                return
            else:
                print("Invalid Input! Please Enter 'Yes' or 'No'.")

# Fungsi untuk menampilkan submenu 'Delete Data'
def delete_menu () :
    while True :
        print("""
        Delete Data Menu :
            1. Delete a Collection by Collection ID
            2. Back to Main Menu
        """)

        menu_input = input("Input Menu That You Want to Run : ").strip()

        if menu_input == "1" : # Panggil fungsi delete data
            delete_data_collection ()
        elif menu_input == "2" : # Kembali ke menu utama
            print("Returning to Main Menu...")
            break
        else:
            print("The Option You Entered is Not Valid! Please Choose Between 1 or 2.")

def delete_data_collection () :
    # Mengecek apakah data_collection kosong
    if not data_collection :
        print("No Collections Available.") # Jika kosong, tampilkan pesan dan keluar dari fungsi
        return  

    # Meminta input Collection ID yang ingin dihapus
    delete_id = input("Input Collection ID of The Item You Want to Delete : ").strip()

    # Jika input kosong, tampilkan pesan error dan keluar
    if not delete_id :
        print("Collection ID Cannot be Empty.")
        return

    # Inisialisasi variabel untuk menyimpan koleksi yang akan dihapus
    collection_to_delete = None
    for item in data_collection : # Loop melalui data_collection untuk mencari ID yang cocok
        if item["Collection ID"] == delete_id :
            collection_to_delete = item # Jika ditemukan, simpan item ke variabel
            break 
    
    # Jika tidak ditemukan ID yang cocok, tampilkan pesan error dan keluar
    if not collection_to_delete :
        print("The Data You are Looking for Does Not Exist!")
        return

    # Menampilkan data yang dipilih untuk dihapus
    print("\nPlease Review The Selected Data :")
    for key, value in collection_to_delete.items() :
        print(f"{key}: {value}")

    # Konfirmasi dari pengguna apakah ingin menghapus data atau tidak
    while True :
        confirm = input("Do You Want to Delete the Data? (Yes/No) : ").strip().lower()
        if confirm == "yes" : # Jika ya, hapus data dari list
            data_collection.remove(collection_to_delete) # .remove() digunakan untuk menghapus item dari list
            print("Data Successfully Deleted! Returning to Delete Data Menu...")
            return
        elif confirm == "no" : # Jika tidak, batalkan penghapusan
            print("Deletion Canceled. Returning to Delete Data Menu...")
            return
        else : # Jika input bukan yes/no, tampilkan pesan error
            print("Invalid Input! Please enter 'Yes' or 'No'.")