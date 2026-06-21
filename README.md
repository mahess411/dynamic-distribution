# Laporan Tugas: Komputasi Paralel & Sistem Terdistribusi
**Topik:** Dynamic Load Balancing (Distribusi Dinamis)  
**Nama:** Hamzah Muhammad Mahesa  
**NRP:** 152024013  

---

## 1. Pendahuluan
Tujuan dari tugas ini adalah mengimplementasikan *Dynamic Load Balancing* menggunakan Python untuk mencapai waktu eksekusi yang optimal. Berbeda dengan distribusi statis yang membagi beban di awal, distribusi dinamis memungkinkan prosesor (worker) mengambil tugas baru segera setelah mereka menyelesaikan tugas sebelumnya.

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
    tasks = range(10) # Total 10 tugas
    
    # Menggunakan Pool untuk distribusi dinamis
    # Prosesor akan mengambil tugas dari queue secara otomatis
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(worker_task, tasks)
        
    for result in results:
        print(result)
