import speedtest

def tampilan_awal():
    print("Speedtest")
    print("1. Jalankan Speedtest")
    print("2. Tampilkan Riwayat Speedtest")
    print("3. Exit Program")
    return input("Pilih menu antara 1-3 : ")

import speedtest

def proses(results):
    st = speedtest.Speedtest()
    
    print("Mencari server terbaik...")
    st.get_best_server()
    
    print("Mengukur kecepatan download...")
    download_speed = st.download() / 1_000_000  # Mengubah ke Mbps
    
    print("Mengukur kecepatan upload...")
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping

    result = {
        'download_speed': download_speed,
        'upload_speed': upload_speed,
        'ping': ping
    }
    results.append(result)  # Menambahkan hasil ke dalam list
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Kecepatan Upload: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

# Fungsi utama

def display_history(results):
    if not results:
        print("Tidak ada riwayat speedtest.")
    else:
        print("\nRiwayat Speedtest:")
        for index, result in enumerate(results):
            print(f"Test {index + 1}: Unduh: {result['download_speed']:.2f} Mbps, Unggah: {result['upload_speed']:.2f} Mbps, Ping: {result['ping']} ms")


def main():
    results = []  # List untuk menyimpan riwayat hasil speedtest
    while True:
        choice = tampilan_awal()
        if choice == '1':
            try:
                proses(results)
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
        elif choice == '2':
            display_history(results)
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main() 
    
# Fungsi utama
# def main():
#     results = []  # List untuk menyimpan riwayat hasil speedtest
#     while True:
#         choice = tampilan_awal()
#         if choice == '1': 
#             proses(results)
#         elif choice == '2':
#             display_history(results)
#         elif choice == '3':
#             print("Keluar dari program.")
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")

# if __name__ == "__main__":
#     main()