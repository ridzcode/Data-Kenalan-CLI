import json
import os

# Lokasi fail untuk menyimpan data
file_name = "kenalan.json"

# Fungsi untuk memuatkan data kenalan dari fail
def load_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

# Fungsi untuk menyimpan data kenalan ke dalam fail
def save_data(contacts):
    with open(file_name, "w") as file:
        json.dump(contacts, file, indent=4)

# Fungsi untuk membersihkan skrin
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menambah kenalan
def add_contact():
    clear_screen()
    print("Tambah Kenalan")
    name = input("Masukkan nama: ")
    dob = input("Masukkan tarikh lahir (dd-mm-yyyy): ")
    phone = input("Masukkan nombor telefon: ")
    email = input("Masukkan email: ")
    image_link = input("Masukkan pautan gambar: ")

    contact = {
        "name": name,
        "dob": dob,
        "phone": phone,
        "email": email,
        "image_link": image_link
    }

    return contact

# Fungsi untuk memaparkan semua kenalan
def display_contacts(contacts):
    clear_screen()
    print("Senarai Kenalan")
    if contacts:
        for idx, contact in enumerate(contacts, 1):
            print(f"\nKenalan {idx}:")
            print(f"Nama: {contact['name']}")
            print(f"Tarikh Lahir: {contact['dob']}")
            print(f"Nombor Telefon: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Pautan Gambar: {contact['image_link']}")
    else:
        print("Tiada kenalan disimpan.")

# Fungsi untuk mencari kenalan
def search_contact(contacts):
    clear_screen()
    print("Cari Kenalan")
    query = input("\nMasukkan nama untuk dicari: ").lower()
    results = [contact for contact in contacts if query in contact['name'].lower()]
    
    if results:
        print("\nHasil carian:")
        display_contacts(results)
    else:
        print("Tiada kenalan yang ditemui dengan nama tersebut.")

# Fungsi untuk mengubah data kenalan
def edit_contact(contacts):
    clear_screen()
    print("Ubah Kenalan")
    display_contacts(contacts)
    if not contacts:
        return

    try:
        idx = int(input("\nMasukkan nombor kenalan untuk diubah: ")) - 1
        if 0 <= idx < len(contacts):
            print("Masukkan maklumat baru (tekan Enter untuk kekalkan data sedia ada):")
            name = input(f"Nama [{contacts[idx]['name']}]: ") or contacts[idx]['name']
            dob = input(f"Tarikh Lahir [{contacts[idx]['dob']}]: ") or contacts[idx]['dob']
            phone = input(f"Nombor Telefon [{contacts[idx]['phone']}]: ") or contacts[idx]['phone']
            email = input(f"Email [{contacts[idx]['email']}]: ") or contacts[idx]['email']
            image_link = input(f"Pautan Gambar [{contacts[idx]['image_link']}]: ") or contacts[idx]['image_link']

            contacts[idx] = {
                "name": name,
                "dob": dob,
                "phone": phone,
                "email": email,
                "image_link": image_link
            }
            save_data(contacts)
            print("Kenalan telah berjaya diubah.")
        else:
            print("Nombor kenalan tidak sah.")
    except ValueError:
        print("Input tidak sah. Masukkan nombor yang betul.")

# Fungsi untuk memadam kenalan
def delete_contact(contacts):
    clear_screen()
    print("Padam Kenalan")
    display_contacts(contacts)
    if not contacts:
        return

    try:
        idx = int(input("\nMasukkan nombor kenalan untuk dipadam: ")) - 1
        if 0 <= idx < len(contacts):
            deleted_contact = contacts.pop(idx)
            save_data(contacts)
            print(f"Kenalan '{deleted_contact['name']}' telah dipadam.")
        else:
            print("Nombor kenalan tidak sah.")
    except ValueError:
        print("Input tidak sah. Masukkan nombor yang betul.")

# Fungsi utama untuk menjalankan aplikasi
def main():
    contacts = load_data()

    while True:
        clear_screen()
        print("Data Kenalan")
        print("\n1. Tambah Kenalan")
        print("2. Lihat Semua Kenalan")
        print("3. Cari Kenalan")
        print("4. Ubah Kenalan")
        print("5. Padam Kenalan")
        print("6. Keluar")
        
        choice = input("Pilih pilihan (1/2/3/4/5/6): ")

        if choice == '1':
            contact = add_contact()
            contacts.append(contact)
            save_data(contacts)
            print("Kenalan telah ditambah.")
        elif choice == '2':
            display_contacts(contacts)
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif choice == '3':
            search_contact(contacts)
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif choice == '4':
            edit_contact(contacts)
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif choice == '5':
            delete_contact(contacts)
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif choice == '6':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak sah. Sila pilih semula.")

if __name__ == "__main__":
    main()
