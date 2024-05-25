def hitung_bunga_tagihan(tagihan_awal, pembayaran_minimum, bunga_bulanan, hari_dalam_siklus):
    sisa_tagihan = tagihan_awal - pembayaran_minimum
    bunga_harian = (bunga_bulanan / 100) / 30
    bunga_pada_sisa_tagihan = sisa_tagihan * bunga_harian * hari_dalam_siklus
    total_tagihan_bulan_berikutnya = sisa_tagihan + bunga_pada_sisa_tagihan
    return bunga_pada_sisa_tagihan, total_tagihan_bulan_berikutnya


def format_rp(nilai):
  """Format nilai sebagai Rupiah dengan titik dan koma."""
  return "Rp {:,.2f}".format(nilai).replace(",", "X").replace(".", ",").replace("X", ".")

tagihan_awal = float(input("Masukkan jumlah tagihan awal: "))
pembayaran_minimum = float(input("Masukkan jumlah pembayaran minimum: "))
bunga_bulanan = float(
    input("Masukkan persentase bunga bulanan (misal 2.25 untuk 2.25%): "))
hari_dalam_siklus = int(input("Masukkan jumlah hari dalam siklus penagihan: "))

bunga, total_tagihan = hitung_bunga_tagihan(
    tagihan_awal, pembayaran_minimum, bunga_bulanan, hari_dalam_siklus)

print(f"Bunga pada sisa tagihan: {format_rp(bunga)}")
print(f"Total tagihan bulan berikutnya: {format_rp(total_tagihan)}")
