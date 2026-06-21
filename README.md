# Laporan Tugas: Komputasi Paralel & Sistem Terdistribusi

**Topik:** Dynamic Load Balancing (Distribusi Dinamis)
**Nama:** Hamzah Muhammad Mahesa
**NRP:** 152024013

---

## 1. Pendahuluan

Tujuan dari tugas ini adalah mengimplementasikan *Dynamic Load Balancing* menggunakan Python untuk mencapai waktu eksekusi yang optimal. Berbeda dengan distribusi statis yang membagi beban kerja di awal, distribusi dinamis memungkinkan setiap prosesor (*worker*) mengambil tugas baru segera setelah menyelesaikan tugas sebelumnya sehingga sumber daya dapat dimanfaatkan secara lebih efisien.

---

## 2. Kode Program

Berikut adalah implementasi menggunakan modul `multiprocessing` di Python:

```python
import multiprocessing
import time
import random

# Fungsi worker untuk mensimulasikan beban kerja dinamis
def worker_task(task_id):
    # Simulasi durasi tugas yang acak (0.1 hingga 1.0 detik)
    sleep_time = random.uniform(0.1, 1.0)
    time.sleep(sleep_time)
    return f"Tugas {task_id} selesai dalam {sleep_time:.2f} detik"

if __name__ == '__main__':
    tasks = range(10)  # Total 10 tugas

    # Menggunakan Pool untuk distribusi dinamis
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(worker_task, tasks)

    for result in results:
        print(result)
```

---

## 3. Penjelasan Program

### a. `multiprocessing.Pool`

`Pool` berfungsi sebagai kumpulan proses (*worker*) yang akan menjalankan tugas secara paralel. Pada program ini digunakan 3 proses worker.

### b. `worker_task()`

Fungsi ini mensimulasikan sebuah tugas dengan waktu eksekusi yang berbeda-beda menggunakan `random.uniform(0.1, 1.0)`. Hal ini menggambarkan kondisi nyata di mana setiap tugas memiliki beban kerja yang tidak sama.

### c. `pool.map()`

Fungsi `pool.map()` mendistribusikan tugas ke worker yang tersedia. Ketika sebuah worker menyelesaikan tugasnya lebih cepat, worker tersebut akan langsung mengambil tugas berikutnya dari antrean.

### d. Dynamic Load Balancing

Mekanisme ini disebut *Dynamic Load Balancing* karena pembagian tugas dilakukan secara dinamis selama proses berjalan. Dengan demikian, worker yang selesai lebih cepat tidak akan menganggur selama masih ada tugas yang belum dikerjakan.

### e. Waktu Eksekusi Optimal

Pendekatan ini membantu mengurangi waktu tunggu dan meningkatkan efisiensi penggunaan prosesor karena seluruh worker dapat bekerja secara bersamaan hingga semua tugas selesai.

---

## 4. Hasil Eksekusi

Lampirkan screenshot hasil eksekusi program pada terminal.

Contoh output:

```text
Tugas 0 selesai dalam 0.23 detik
Tugas 1 selesai dalam 0.45 detik
Tugas 2 selesai dalam 0.17 detik
Tugas 3 selesai dalam 0.81 detik
Tugas 4 selesai dalam 0.29 detik
Tugas 5 selesai dalam 0.67 detik
Tugas 6 selesai dalam 0.31 detik
Tugas 7 selesai dalam 0.54 detik
Tugas 8 selesai dalam 0.19 detik
Tugas 9 selesai dalam 0.72 detik
```

---

## 5. Kesimpulan

Implementasi Dynamic Load Balancing menggunakan modul `multiprocessing` memungkinkan pembagian tugas secara otomatis kepada worker yang tersedia. Pendekatan ini meningkatkan efisiensi penggunaan sumber daya dan mengurangi waktu tunggu dibandingkan metode distribusi statis.
