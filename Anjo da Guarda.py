import psutil
import time

def is_tibia_running():
    return any(
        process.info['name'] and process.info['name'].lower() == 'client' # Mude o nome para client.exe se pretende usar no Windows.
        for process in psutil.process_iter(['name'])
    )  

def main(): 

    while True:
        if is_tibia_running():
            time.sleep(1)
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()