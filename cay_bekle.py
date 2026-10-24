#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Cay Bekleyisi Simulatoru
Cay demlenirken evrenin genislemesini gozlemleyen kod.
"""

import time
import random
import sys

def cay_demle(sure=7):
    print("Caydanlik ocağa kondu. Kuantum cay partikulleri harekete geciyor...")
    for i in range(sure):
        print(f"Bekleniyor... {i+1}/{sure} dakika (aslinda saniye ama hissetmiyorsun)")
        time.sleep(1)
        if random.random() < 0.3:
            print("  -> Komsu 'cay bitti mi?' diye bagirdi. Cevap: HENUZ!")
    print("\nCAY DEMENDI! Ama sen hala bekliyorsun cunku bu bir simulator.")
    print("Tebrikler, bir dakika daha yaslandin.")

if __name__ == "__main__":
    print("=== SONSÜZ ÇAY BEKLEYİŞİ SİMÜLATÖRÜ v1.0 ===")
    print("Bu kod gercekten calisir. Gercekten bekletir.")
    cay_demle(5)
    print("\nProgram sona erdi. Cay ic ve devam et.")

# Gizli: # Base64: VMO0Z3IgbWVjbGlzIHPDvHLDvMOnZWxlcmluaW4gY2F5IGljaW5kZW4gZ2VsaXIgY2FsaXNtYXNpCg== (decode et, sadece sakladim)
