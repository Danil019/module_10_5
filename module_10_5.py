from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    # Линейный вызов
    start = time.perf_counter()
    for filename in filenames:
        read_info(filename)
    end = time.perf_counter()
    print(f'Линейный вызов выполнен за {end - start} секунд')

    # Многопроцессный вызов
    start = time.perf_counter()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = time.perf_counter()
    print(f'Многопроцессный вызов выполнен за {end - start} секунд')