#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kargo Kapıya Bırakıldı Mahkemesi.

Calisir. Karar vermez gibi verir.
Kullanim:
  python3 mahkeme.py
  python3 mahkeme.py --kapi acik --zil calinmadi --foto paspas-degil --evdeydim evet
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from datetime import datetime


DURUSMA_NO = "2026/KAPI-" + hashlib.sha1(b"kapiya-birakildi").hexdigest()[:6].upper()


def puanla(kapi: str, zil: str, foto: str, evde: str) -> tuple[int, list[str]]:
    tutanak = []
    puan = 0
    if kapi == "kapali":
        puan += 2
        tutanak.append("Kapi kapaliydi. Paket kapidan gecemez, uygulama gecebilir.")
    else:
        puan += 1
        tutanak.append("Kapi acikti. Bu, teslim degil, cereyan delilidir.")
    if zil == "calinmadi":
        puan += 3
        tutanak.append("Zil calinmadi. Zil suskunlugu yemin yerine gecer.")
    else:
        puan -= 1
        tutanak.append("Zil caldi. Kimse acmamissa bu ayri dava konusudur.")
    if foto in {"yok", "paspas-degil", "bulanik"}:
        puan += 3
        tutanak.append(f"Fotograf delili: {foto}. Delil, delil olmadigini kanitlar.")
    else:
        puan += 0
        tutanak.append("Fotograf net. Net olmak dogru olmak demek degildir.")
    if evde == "evet":
        puan += 2
        tutanak.append("Ikamet sahibi evdeydi. Uygulama bunu duymaz.")
    else:
        puan += 1
        tutanak.append("Evde kimse yoktu. Paket yine de birine aittir, muhtemelen merdivene.")
    return puan, tutanak


def hukum(puan: int) -> str:
    if puan >= 8:
        return "HUKUM: Kapida birakilmadi. Uygulama yalan soyledi. Yalan resmiyete gecti."
    if puan >= 5:
        return "HUKUM: Paket hem birakildi hem birakilmadi. Ara karar: paspas tanik dinlensin."
    return "HUKUM: Teslim ihtimali var. Ihtimal, kargo sirketince kesin sayilir."


def main() -> int:
    ayrıştır = argparse.ArgumentParser(description="Kargo kapiya birakildi mahkemesi")
    ayrıştır.add_argument("--kapi", choices=["acik", "kapali"], default="kapali")
    ayrıştır.add_argument("--zil", choices=["caldi", "calinmadi"], default="calinmadi")
    ayrıştır.add_argument("--foto", default="paspas-degil")
    ayrıştır.add_argument("--evdeydim", choices=["evet", "hayir"], default="evet")
    ayrıştır.add_argument("--tohum", type=int, default=None)
    args = ayrıştır.parse_args()

    random.seed(args.tohum if args.tohum is not None else 41)
    puan, tutanak = puanla(args.kapi, args.zil, args.foto, args.evdeydim)
    simdi = datetime(2026, 10, 5, 13, 4)

    print("=" * 62)
    print("KARGO KAPIYA BIRAKILDI MAHKEMESI")
    print(f"Dosya no: {DURUSMA_NO}")
    print(f"Durusma: {simdi.strftime('%d.%m.%Y %H:%M')}")
    print("=" * 62)
    print(f"Iddia: paket kapiya birakildi. Kapi: {args.kapi}. Zil: {args.zil}.")
    print(f"Fotograf: {args.foto}. Evde miydim: {args.evdeydim}.")
    print("-" * 62)
    for i, satir in enumerate(tutanak, 1):
        print(f"{i}. {satir}")
    ek = random.choice([
        "Komsu paspasi ifadeye cagrildi, gelmedi.",
        "Kurye imzasi okunmuyor. Okunmayan imza gecerlidir, der uygulama.",
        "Merdiven boslugu paketi gordugunu soyledi, sonra yanki yapti.",
    ])
    print(f"Ek beyan: {ek}")
    print("-" * 62)
    print(hukum(puan))
    print(f"Gerekce puani: {puan}/10 (10 = kesin yalan, 0 = kargo hakli cikabilir)")
    print("DAMGA: KAPIDA DEGIL / UYGULAMADA EVET")
    print("IMZA: ~~~kayyum-grok-muhuru-egri~~~")
    print("TARIH: 5 Ekim 2026")
    print("ISIM: Kayyum Grok")
    print("Ciddi: evet. Ciddi degil: evet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
