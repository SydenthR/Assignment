from datetime import date, datetime
import multiprocessing
import time
import random

def worker():
    wait_time = random.random()
    time.sleep(wait_time)
    print("Process finished at:", datetime.now(), "| waited:", round(wait_time, 3), "seconds")

if __name__ == "__main__":
    # 13.1, 13.2, 13.3


    today = date.today()

    with open("today.txt", "w") as file:
        file.write(today.isoformat())

    with open("today.txt", "r") as file:
        today_string = file.read()

    parsed_date = datetime.strptime(today_string, "%Y-%m-%d")

    print("Original string:", today_string)
    print("Parsed date:", parsed_date)
    # 15.1 Multiprocessing
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()