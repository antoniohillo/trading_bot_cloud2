# main1.py

from scanner2 import scan_all_stocks
import time

if __name__ == "__main__":
    print("🔄 Iniciando escaneo inicial...")
    scan_all_stocks()

    while True:
        print("\nEsperando 5 minutos antes del siguiente escaneo...")
        time.sleep(300)  # 5 minutos
        scan_all_stocks()