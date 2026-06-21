import multiprocessing
import time
import random

# Fungsi yang mensimulasikan tugas dengan durasi berbeda
def worker_task(task_id):
    sleep_time = random.uniform(0.1, 1.0) # Simulasi beban kerja dinamis
    time.sleep(sleep_time)
    return f"Tugas {task_id} selesai dalam {sleep_time:.2f} detik"

if __name__ == '__main__':
    tasks = range(10) # 10 tugas yang harus dikerjakan
    
    # Pool akan otomatis mengatur distribusi tugas ke prosesor yang tersedia
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(worker_task, tasks)
        
    for result in results:
        print(result)