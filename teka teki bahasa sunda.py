Lewati ke konten
Riwayat obrolan

Anda bilang:
import random  # Daftar soal dan jawaban soal_jawaban = {     "Hayam tukung sapatu, sok clak-clak dina waktu": "Jalma nu nincak kokotor",     "Lamun leutik jadi babaturan, lamun gede jadi musuh": "Seuneu",     "Ka luhur mah siga andjing, ka handap mah siga dogdog": "Payung",     "Sapanjang jalan gegerewekan, tapi teu boga sungut": "Bilahan awi",     "Abdi alit sok diseuseulan, abdi gede sok dipaen": "Parudan",     "Hayang teuing geura gedé, sanggeus gedé kalah kahariwang": "Anak hayam",     "Lamun diasakan beureum, lamun atah bodas": "Aki-aki",     "Dicekel ipis, ditincak kandel": "Hihideung",     "Gedé panjang, lamun leutik boga buntut": "Kalimah",     "Akar nyebar di awang-awang, daun ngumpul di handapeun": "Janggot",     "Leuheung mun peuting, leuheung mun hujan": "Usum",     "Saha nu sok nangkeupan gunung bari teu bisa ngahontal": "Gordeng",     "Leutik konéng ngagantung, gedé beureum baradag": "Balon",     "Boga buntut dina sirah": "Garpuh" }  def main():     """Fungsi utama untuk menjalankan permainan tebak-tebakan."""      print("Wilujeng sumping dina kaulinan tebak-tebakan Sunda!")     print("Cobi téangan jawaban anu bener.\n")      # Acak urutan soal     daftar_soal = list(soal_jawaban.keys())     random.shuffle(daftar_soal)      skor = 0     for i, soal in enumerate(daftar_soal[:15]):  # Ambil 15 soal pertama         print(f"Soal ka-{i + 1}: {soal}")         jawaban_pamake = input("Jawaban anjeun: ")          jawaban_bener = soal_jawaban[soal].lower()         jawaban_pamake = jawaban_pamake.lower()          if jawaban_pamake == jawaban_bener:             print("Leres pisan!\n")             skor += 1         else:             print(f"Salah. Jawaban anu leres nyaéta: {soal_jawaban[soal]}\n")      print(f"Kaulinan réngsé! Skor anjeun: {skor} / 15")  if __name__ == "__main__":     main()     buatkan versi streamlit 
ChatGPT bilang:
Berikut versi Streamlit dari permainan tebak-tebakan Sunda kamu.
Kodenya sudah disesuaikan agar bisa berjalan interaktif di web Streamlit, tanpa perlu input() di terminal.

Kamu bisa salin ini ke file bernama main.py lalu jalankan di Streamlit. 👇

import streamlit as st
import random

# Daftar soal dan jawaban
soal_jawaban = {
    "Hayam tukung sapatu, sok clak-clak dina waktu": "Jalma nu nincak kokotor",
    "Lamun leutik jadi babaturan, lamun gede jadi musuh": "Seuneu",
    "Ka luhur mah siga andjing, ka handap mah siga dogdog": "Payung",
    "Sapanjang jalan gegerewekan, tapi teu boga sungut": "Bilahan awi",
    "Abdi alit sok diseuseulan, abdi gede sok dipaen": "Parudan",
    "Hayang teuing geura gedé, sanggeus gedé kalah kahariwang": "Anak hayam",
    "Lamun diasakan beureum, lamun atah bodas": "Aki-aki",
    "Dicekel ipis, ditincak kandel": "Hihideung",
    "Gedé panjang, lamun leutik boga buntut": "Kalimah",
    "Akar nyebar di awang-awang, daun ngumpul di handapeun": "Janggot",
    "Leuheung mun peuting, leuheung mun hujan": "Usum",
    "Saha nu sok nangkeupan gunung bari teu bisa ngahontal": "Gordeng",
    "Leutik konéng ngagantung, gedé beureum baradag": "Balon",
    "Boga buntut dina sirah": "Garpuh"
}

# Inisialisasi sesi
if "skor" not in st.session_state:
    st.session_state.skor = 0
if "index" not in st.session_state:
    st.session_state.index = 0
if "soal_acak" not in st.session_state:
    st.session_state.soal_acak = random.sample(list(soal_jawaban.keys()), 15)
if "selesai" not in st.session_state:
    st.session_state.selesai = False

st.title("🎯 Kaulinan Tebak-tebakan Sunda")
st.write("Wilujeng sumping dina kaulinan tebak-tebakan Sunda! Cobi téangan jawaban anu leres.")

# Jika permainan belum selesai
if not st.session_state.selesai:
    soal = st.session_state.soal_acak[st.session_state.index]
    st.subheader(f"Soal ka-{st.session_state.index + 1}")
    st.write(f"🗣️ {soal}")

    jawaban_pamake = st.text_input("Jawaban anjeun:", key=f"jawaban_{st.session_state.index}")

    if st.button("Kirim Jawaban"):
        if jawaban_pamake.strip().lower() == soal_jawaban[soal].lower():
            st.success("✅ Leres pisan!")
            st.session_state.skor += 1
        else:
            st.error(f"❌ Salah. Jawaban anu leres nyaéta: {soal_jawaban[soal]}")

        st.session_state.index += 1

        if st.session_state.index >= 15:
            st.session_state.selesai = True
        st.experimental_rerun()

else:
    st.subheader("🏁 Kaulinan Réngsé!")
    st.write(f"Skor anjeun: **{st.session_state.skor} / 15** 🎉")

    if st.button("Main deui"):
        st.session_state.skor = 0
        st.session_state.index = 0
        st.session_state.soal_acak = random.sample(list(soal_jawaban.keys()), 15)
        st.session_state.selesai = False
        st.experimental_rerun()
💡 Cara Menjalankan
Simpan file ini sebagai main.py.

Buka terminal (atau di Chromebook: buka VS Code, Replit, atau Python Editor).

Jalankan perintah:

streamlit run main.py
Akses di browser — biasanya di http://localhost:8501.

Apakah kamu ingin saya bantu tambahkan fitur skor langsung dan leaderboard sederhana biar bisa dipakai di kelas juga?




Tidak ada file yang dipilihTidak ada file yang dipilih
ChatGPT dapat membuat kesalahan. Periksa info penting. Lihat Preferensi Cookie.
