import random
import time
import datetime

def generate_random_log():
    log_levels = ['INFO', 'DEBUG']
    log_messages = ['Task completed successfully', 'Great progress made', 'Everything is running smoothly', 'Success achieved']

    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_level = random.choice(log_levels)
    log_message = random.choice(log_messages)

    log_entry = f'{current_time} [{log_level}] - {log_message}'
    return log_entry

def main():
    while True:
        log_entry = generate_random_log()
        print(log_entry)
        time.sleep(1)  # Optional delay between logs

if __name__ == "__main__":
    main()
