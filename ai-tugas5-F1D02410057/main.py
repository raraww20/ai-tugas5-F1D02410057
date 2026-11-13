import json
import textwrap


def baca_kb(nama_file):
    with open(nama_file, encoding="utf-8") as f:
        return json.load(f)


def cari_fakta_dasar(kb):
    semua_hasil = [aturan["maka"] for aturan in kb["aturan"]]
    fakta_dasar = []
    for aturan in kb["aturan"]:
        for fakta in aturan["jika"]:
            if fakta not in semua_hasil and fakta not in fakta_dasar:
                fakta_dasar.append(fakta)
    return fakta_dasar


def cari_kesimpulan_akhir(kb):
    semua_syarat = []
    for aturan in kb["aturan"]:
        semua_syarat.extend(aturan["jika"])
    return [aturan["maka"] for aturan in kb["aturan"]
            if aturan["maka"] not in semua_syarat]


def syarat_terpenuhi(aturan, memori):
    jumlah_ada = sum(1 for syarat in aturan["jika"] if syarat in memori)
    if aturan["mode"] == "dan":
        return jumlah_ada == len(aturan["jika"])
    return jumlah_ada >= 1


def forward_chaining(kb, fakta_awal):
    memori = list(fakta_awal)
    asal = {}
    urutan = []
    while True:
        cocok = []
        for aturan in kb["aturan"]:
            if syarat_terpenuhi(aturan, memori) and aturan["maka"] not in memori:
                cocok.append(aturan)
        if not cocok:
            break
        aturan = cocok[0]
        memori.append(aturan["maka"])
        asal[aturan["maka"]] = aturan
        urutan.append(aturan)
    return memori, asal, urutan


def cetak_alasan(fakta, asal, memori, tingkat=1):
    if fakta not in asal:
        return
    aturan = asal[fakta]
    syarat_dipakai = [s for s in aturan["jika"] if s in memori]
    print("  " * tingkat + fakta + " <- " + aturan["id"]
          + " (" + ", ".join(syarat_dipakai) + ") ["
          + ", ".join(aturan["sumber"]) + "]")
    for syarat in syarat_dipakai:
        cetak_alasan(syarat, asal, memori, tingkat + 1)


def tanya_ya_tidak(teks):
    while True:
        jawab = input(teks).strip().lower()
        if jawab in ("y", "t"):
            return jawab == "y"
        print("   Ketik y untuk Ya atau t untuk Tidak.")


def satu_diagnosa(kb, fakta_dasar, kesimpulan_akhir):
    print( kb["judul"])
    print("Jawab pertanyaan dengan y (ya) atau t (tidak).")
    fakta_awal = []
    for nomor, fakta in enumerate(fakta_dasar, start=1):
        if tanya_ya_tidak(f"{nomor}. {kb['pertanyaan'][fakta]} (y/t) > "):
            fakta_awal.append(fakta)

    print("\nFakta awal:")
    print(", ".join(fakta_awal) if fakta_awal else "(tidak ada)")
    memori, asal, urutan = forward_chaining(kb, fakta_awal)

    print("\nProses Forward Chaining:")
    for siklus, aturan in enumerate(urutan, start=1):
        print(f"Siklus {siklus}: {aturan['id']} -> {aturan['maka']}")
    print(f"Siklus {len(urutan)+1}: tidak ada aturan baru, berhenti")

    kesimpulan = [aturan["maka"] for aturan in urutan
                  if aturan["maka"] in kesimpulan_akhir]
    print("\nKesimpulan:")
    if not kesimpulan:
        print("Tidak ada kesimpulan dari fakta yang diberikan.")
    else:
        for item in kesimpulan:
            print("- " + item)
        print("\nAlasan:")
        for item in kesimpulan:
            cetak_alasan(item, asal, memori)

    print("\nCatatan:")
    print(textwrap.fill(kb["batas"], width=85))
    print()


def main():
    kb = baca_kb("kb_gili.json")
    fakta_dasar = cari_fakta_dasar(kb)
    kesimpulan_akhir = cari_kesimpulan_akhir(kb)
    while True:
        satu_diagnosa(kb, fakta_dasar, kesimpulan_akhir)
        if not tanya_ya_tidak("Periksa kondisi lain? (y/t) > "):
            break


if __name__ == "__main__":
    main()
