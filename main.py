import psutil
import logging
from time import sleep
import colorlog


def get_cpu_metrics():
    return psutil.cpu_percent()


def get_memory_metrics():
    used_memory = psutil.virtual_memory().used
    total_memory = psutil.virtual_memory().total
    used_percent = (used_memory / total_memory) * 100
    return round(used_percent, 1)


def get_disk_metrics(path: str):
    total_disk = psutil.disk_usage(path).total
    used_disk = psutil.disk_usage(path).used
    used_percent = (used_disk / total_disk) * 100
    return round(used_percent, 1)


def get_active_process_count():
    return len(list(psutil.process_iter()))


def generate_resource_alert(resource_type: str, percentage_usage: float, logger: logging):

    message = f"{resource_type.upper()} is at {percentage_usage}% usage."

    if percentage_usage > RESOURCE_CRITICAL_THRESHOLD:
        logger.critical(message)
    elif percentage_usage > RESOURCE_WARNING_THRESHOLD:
        logger.warning(message)
    else:
        logger.info(message)


LOGGING_INTERVAL = 3
RESOURCES = {'CPU': get_cpu_metrics, 'RAM': get_memory_metrics, 'DISK': get_disk_metrics}
DISKS_TO_MONITOR = ['/']    # Add more disks to monitor
RESOURCE_CRITICAL_THRESHOLD = 90
RESOURCE_WARNING_THRESHOLD = 60


print("[+] Monitoring Started.")

# Setting up logging format and logging level
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)
handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter('%(white)s%(asctime)s%(reset)s - %(log_color)s%(levelname)s: %(message)s%(reset)s', datefmt='%Y-%m-%d %H:%M:%S', log_colors={'INFO': 'green', 'WARNING': 'yellow', 'CRITICAL': 'red'})
handler.setFormatter(formatter)
logger.addHandler(handler)


while True:
    try:
        sleep(LOGGING_INTERVAL)
        logger.info(f"Number of active processes: {get_active_process_count()}")
        for resource_name, resource_metrics in RESOURCES.items():
            if resource_name.upper() == 'DISK':
                for path in DISKS_TO_MONITOR:
                    generate_resource_alert(f"{resource_name} {path}", resource_metrics(path), logger)
            else:
                generate_resource_alert(resource_name, resource_metrics(), logger)
    except KeyboardInterrupt:
        print("[x] Monitoring Stopped.")
        exit(0)

