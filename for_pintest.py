import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        print(f"Функция выполнилась за: {formatted_time}")
        return result

    return wrapper

@execution_time
def generate_all_numbers(filename, quantity_digits, buffer_size = 10000):
    base_number = '0' * quantity_digits
    buffer = []

    with open(filename, 'a') as file:
        for i_num in range(10 ** quantity_digits):
            last_num = len(str(i_num))
            password = base_number[:-last_num] + str(i_num)
            buffer.append(password + '\n')

            if len(buffer) >= buffer_size:
                file.write(''.join(buffer))
                buffer.clear()

        if buffer:
            file.write(''.join(buffer))


if __name__ == '__main__':
    generate_all_numbers('passwords.txt', 9)