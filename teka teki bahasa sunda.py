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

# Inisialisasi session state
if "skor" not in st.session_state:
    st.session_state.skor = 0
if "index" not in st.session_state:
    st.session_state.index = 0
if "soal_acak" not in st.session_state:
    st.session_state.soal_acak = random.sample(list(soal_jawaban.keys()), 15)
if "selesai" not in st.session_state:
    st.session_state.selesai = False

# Judul dan petunjuk
st.title("🎯 Kaulinan Tebak-tebakan Sunda")
st.write("Wilujeng sumping! Cobi téangan jawaban anu leres.")

# Tampilkan skor sementara
st.info(f"📊 Skor ayeuna: {st.session_state.skor} / {st.session_state.index}")

# Permainan belum selesai
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

# Permainan selesai
else:
    st.subheader("🏁 Kaulinan Réngsé!")
    st.success(f"Skor anjeun: **{st.session_state.skor} / 15** 🎉")

    if st.button("🔁 Main deui"):
        st.session_state.skor = 0
        st.session_state.index = 0
        st.session_state.soal_acak = random.sample(list(soal_jawaban.keys()), 15)
        st.session_state.selesai = False
        st.experimental_rerun()
