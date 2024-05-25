import streamlit as st
from streamlit_option_menu import option_menu  
from PIL import Image

# Streamlit theme
primaryColor="#4bffe3"
backgroundColor="#d3efec"
secondaryBackgroundColor="#c3e6e6"
textColor="#000000"

# Create a dictionary to store the medicine information
medicines = {
    "Ibuprofen": {
        "image": "ibuprofen.jpeg",
        "type": "Anti-Inflamasi (Obat radang)",
        "category": "Obat bebas disertai resep dokter",
        "side_effects": "Sakit perut, mulas, diare, sembelit, kembung, gas, pusing, sakit kepala, gugup, atau ruam..",
        "description": "Ibuprofen adalah obat anti-inflamasi (Obat radang) yang digunakan untuk menghilangkan rasa sakit, mengurangi peradangan, dan mengurangi demam.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/ibuprofen-400-mg-10-tablet"
    },
    "Paracetamol": {
        "image": "paracetamol.jpeg",
        "type": "Analgesik (Obat nyeri)",
        "category": "Obat bebas disertai resep dokter",
        "side_effects": "Mual, muntah, sakit perut, kehilangan nafsu makan, dan sakit kepala.",
        "description": "Paracetamol adalah tipe obat analgesik (Obat nyeri) yang digunakan untuk menghilangkan rasa sakit dan mengurangi demam. Hal ini juga digunakan untuk menghilangkan rasa sakit dalam kondisi seperti arthritis, migrain, dan sakit gigi.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/paracetamol-500-mg-10-kaplet"
    },
    "Aspirin": {
        "image": "aspirin.png",
        "type": "Analgesik (Obat nyeri)",
        "category": "Obat bebas disertai resep dokter",
        "side_effects": "Sakit perut, mulas, diare, sembelit, kembung, gas, pusing, sakit kepala, gugup, atau ruam.",
        "description": "Aspirin adalah tipe obat analgesik (Obat nyeri) yang digunakan untuk mengurangi rasa sakit, demam, dan peradangan. Obat ini juga digunakan untuk mencegah serangan jantung, stroke, dan pembekuan darah.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/cardio-aspirin-100-mg-10-tablet"
    },
    "Amoxicillin": {
        "image": "amoxicillin.jpeg",
        "type": "Antibiotik (infeksi bakteri)",
        "category": "Obat dengan resep dokter",
        "side_effects": "mual, muntah, diare, sakit perut, ruam kulit, dan infeksi jamur vagina.",
        "description": "Amoxicillin adalah tipe antibiotik (infeksi bakteri) yang digunakan untuk mengobati sejumlah infeksi bakteri.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/amoxicillin-500-mg-10-tablet"
    },
    "Azithromycin": {
        "image": "azithromycin.jpeg",
        "type": "Antibiotik (infeksi bakteri)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Mual, muntah, diare, sakit perut, dan sakit kepala.",
        "description": "Azithromycin adalah tipe antibiotik (infeksi bakteri) yang digunakan untuk mengobati sejumlah infeksi bakteri.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/azithromycin-500-mg-tablet"
        },
    "Buspirone": {
        "image": "buspirone.png",
        "type": "Anticemas (Obat cemas)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Gata-gatal; sulit bernapas; pembengkakan pada wajah, bibir, lidah, atau tenggorokan. Tidak dianjurkan untuk ibu hamil, ibu menyusui, dan anak-anak.",
        "description": "Buspirone adalah obat untuk mengatasi gangguan kecemasan dalam jangka pendek.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/xiety-10-mg-10-tablet"
        },
    "Escitalopram": {
        "image": "escitalopram.jpeg",
        "type": "Anticemas (Obat cemas)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Mual, mulut kering, sulit tidur, sembelit, kelelahan, mengantuk, pusing, dan peningkatan kelenjar keringat.",
        "description": "Azithromycin adalah obat untuk meredakan kecemasan.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/cipralex-tablet-10-mg"
        },
    "Propranolol": {
        "image": "propanolol.webp",
        "type": "Anti-aritmia (Obat Jantung)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Mudah lelah, pusing, penurunan denyut jantung, gangguan tidur, perubahan mood, dan masalah gastrointestinal seperti mual dan diare. Efek samping yang lebih jarang meliputi penurunan libido, masalah ereksi, dan reaksi alergi.",
        "description": "Propranolol adalah obat jantung untuk menghambat aksi adrenergik pada reseptor beta.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/propranolol-10-mg-10-tablet"
        },
    "Verapamil": {
        "image": "verapamil.jpeg",
        "type": "Anti-aritmia (Obat Jantung)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Sakit kepala, pusing, sembelit, edema (pembengkakan), dan peningkatan risiko gangguan konduksi jantung. Efek samping yang lebih seius termasuk penurunan denyut jantung, reaksi alergi, dan efek toksik pada hati.",
        "description": "Verapamil adalah obat yang digunakan untuk mengobati hipertensi (tekanan darah tinggi), angina (nyeri dada akibat kurangnya aliran darah ke jantung), dan aritmia (ketidakaturan detak jantung).",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/isoptin-80-mg-10-tablet"
    },
    "Diazepam": {
        "image": "diazopam.png",
        "type": "Antikonvulsan (Obat Kejang)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Mudah kantuk, penurunan kewaspadaan, penurunan koordinasi, dan kebingungan. Penggunaan jangka panjang dapat menyebabkan ketergantungan dan toleransi terhadap obat, serta efek samping yang lebih serius seperti depresi pernapasan.",
        "description": "Diazepam adalah obat yang digunakan untuk mengobati kecemasan, gangguan kejang, dan kejang epilepsi. Juga digunakan sebelum prosedur medis untuk membantu meredakan kecemasan dan ketegangan otot.",
        "buy_link": "https://e-katalog.lkpp.go.id/katalog/produk/detail/74164674"
    },
    "Klonazepam": {
        "image": "Clonazepam.jpg",
        "type": "Antikonvulsan (Obat Kejang)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Mudah kantuk, penurunan kewaspadaan, penurunan koordinasi, dan kebingungan. Penggunaan jangka panjang dapat menyebabkan ketergantungan dan toleransi terhadap obat, serta efek samping yang lebih serius seperti depresi pernapasan.",
        "description": "Klonazepam adalah obat yang digunakan untuk mengobati gangguan kecemasan, epilepsi (kejang), dan serangan panik. Ini juga dapat digunakan sebagai pengobatan tambahan untuk gangguan kejang yang disebabkan oleh epilepsi.",
        "buy_link": "-"
    },
    "Paroxetine": {
        "image": "paroxetine.webp",
        "type": "Antidepresan (Obat Depresi)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Mual, muntah, sakit kepala, gangguan tidur, peningkatan kelenjar keringat, penurunan nafsu makan, dan disfungsi seksual. Penggunaan jangka panjang juga dapat menyebabkan penarikan atau gejala penarikan jika penggunaan dihentikan secara tiba-tiba.",
        "description": "Paroxetine adalah obat yang digunakan untuk mengobati berbagai kondisi, termasuk depresi, gangguan kecemasan, gangguan obsesif-kompulsif (OCD), gangguan panik, dan gangguan stress pasca-trauma (PTSD).",
        "buy_link": "https://blibli.onelink.me/GNtk/nhwd5xe1 "
    },
    "Diphenhydramine": {
        "image": "Diphenhydramine.jpeg",
        "type": "Antiemetik (Obat Alergi)",
        "category": "Obat bebas",
        "side_effects": "Kantuk, mulut kering, pusing dan gangguan penglihatan. Penggunaan jangka panjang dapat menyebabkan efek samping yang lebih serius seperti gangguan kognitif, penurunan kemampuan motorik, dan gangguan kardiovaskular.",
        "description": "Diphenhydramine adalah obat yang digunakan untuk meredakan gejala alergi seperti gatal-gatal, bersin, dan pilek. Ini juga dapat digunakan sebagai obat tidur karena efek kantuknya.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/otede-4-tablet"
    },
    "Metoclopramide": {
        "image": "metoclopramide.webp",
        "type": "Antiemetik (Obat Alergi)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Kelelahan, kantuk, sakit kepala, diare, dan gangguan menstruari pada wanita. Efek samping yang lebih serius termasuk gangguan gerakan seperti diskinesia tardif (gangguan gerakan yang tidak disengaja), serta peningkatan risiko depresi akut pada orang tua.",
        "description": "Metoclopramide adalah obat yang digunakan untuk mengobati mual dan muntah yang disebabkan oleh aleh alergi ataupun berbagai kondisi medis.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/metoclopramide-10-mg-10-tablet"
    },
    "Penisilin": {
        "image": "ampicillin.jpg",
        "type": "Antibiotik (infeksi bakteri)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Mual, muntah, diare, sakit perut, ruam.",
        "description": "Penisilin adalah antibiotik yang digunakan untuk mengobati sejumlah infeksi bakteri.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/ampicillin-500-mg-10-tablet"
    },
    "Sefalospirin": {
        "image": "Sefalospirin.webp",
        "type": "Antibiotik (infeksi bakteri)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Ruam dan infeksi jamur.",
        "description": "Sefalospirin adalah antibiotik yang digunakan untuk mengobati sejumlah infeksi kulit, saluran pernapasan atas, dan saluran kemih.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/staforin-125-mg-dry-sirup-60-ml"
    },
    "Coumarin": {
        "image": "Coumarin.webp",
        "type": "Antikoagulan dan Trombolitik (Penggumpalan darah)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Pendarahan hebat.",
        "description": "Coumarin adalah obat yang bekerja dengan menghambat kerja vitamin K dalam mengaktifkan faktor-faktor pembekuan darah dan untuk menghentikan pendarahan sehingga mencegah adanya penggumpalan darah.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/liproqy-6-kapsul"
    },
    "Oralit": {
        "image": "oralit.jpg",
        "type": "Antidiare (Obat diare)",
        "category": "Obat bebas",
        "side_effects": "Perut kembung dan mata bengkak.",
        "description": "Oralit adalah obat yang digunakan untuk mencegah diare dan menambahan ion tubuh pada saat diare.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/oralit-200-4-1-g-1-sachet"
    },
    "Loperamide": {
        "image": "Loperamide.jpeg",
        "type": "Antidiare (Obat diare)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Semmbelit, perut kembung, sakit kepala, mual, dan pusing.",
        "description": "Loperamide adalah obat yang digunakan untuk mengurangi frekuensi diare. Obat ini sering digunakan pada Gastroenteritis, penyakit radang usus, dan sindrom usus pendek.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/loperamide-2-mg-10-tablet"
    },
    "Itraconazole": {
        "image": "Itraconazole.webp",
        "type": "Antijamur (Obat jamur)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Mual, muntah, diare, sakit perut, dan sakit kepala.",
        "description": "Itraconazole adalah obat anti jamur akibat infeksi jamur yang di gunakan khusus untuk orang dewasa. Bagian-bagian yang terinfeksi adalah kuku, kuku kaki, paru-paru, dan mulut (kerongkongan).",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/itraconazole-100-mg-10-kapsul"
    },
    "Clotrimazole": {
        "image": "Clotrimazole.webp",
        "type": "Antijamur (Obat jamur)",
        "category": "Obat bebas disertai resep dokter",
        "side_effects": "Kram perut, diare, gatal-gatal, mual atau muntah, perubahan pada indra perasa.",
        "description": "Clotrimazole digunakan untuk mencegah pertumbuhan jamur pada mulut, tenggrokan, liang telinga, vagina (candidiasis vaginalis) dan infeksi jamur lainya seperti, tinea pedis (jamur di jari-jari kaki), kurap, panu serta infeksi jamur yang menyebabkan pencerahan atau penggelapan pada kulit leher, dada, lengan, atau kaki.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/erphamazol-1-krim-5-g"
    },
    "Voriconazole": {
        "image": "Voriconazole.jpg",
        "type": "Antijamur (Obat jamur)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Penglihatan kabur, perubahan warna penglihatan, gangguan penglihatan, demam, mual, ruam kulit, muntah, kedinginan.",
        "description": "Voriconazole adalah obat antijamur yang disebut triazol yang berguna untuk mengobati infeksi jamur seperti spergillosis invasif(yang dimulai dari paru-paru) dan kandidiasis esofagus (bercak putih di mulut dan tenggorokan).",
        "buy_link": "https://www.blibli.com/p/vfend-200-mg-box-10-tablet/ps--NAF-70062-02011"
    },
    "Chlorphenamine": {
        "image": "Chlorphenamine.jpg",
        "type": "Antihistamin",
        "category": "Obat bebas disertai resep dokter",
        "side_effects": "Pusing, kantuk, sembelit, penglihatan kabur, merasa gugup atau gelisah.",
        "description": "Chlorphenamine atau chlorpheniramine membantu meredakan gejala pilek dan alergi, seperti pilek, bersin, serta mata gatal dan berair. Chlorphenamine juga membantu meringankan kondisi alergi kulit seperti gatal-gatal dan ruam gatal akibat rhinitis alergi atau selesma.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/ctm-chlorpheniramine-maleate-4-mg-10-tablet"
    },
    "Brompheniramine": {
        "image": "Brompheniramine.jpeg",
        "type": "Antihistamin (Obat alergi dan pilek)",
        "category": "Obat bebas",
        "side_effects": "Rasa kantuk, sembelit, kulit atau wajah memerah (terasa hangat, kemerahan dan geli), mulut atau tenggorokan kering, merasa gelisah atau gugup.",
        "description": "Brompheniramine adalah obat generik yang digunakan untuk mengobati beberapa penyakit yang disebabkan oleh alergi. Brompheniramine sering juga digunakan untuk mengobati nasofaringitis atau pilek yang akut.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/alco-plus-sirup-100-ml"
    },
    "Naproxen": {
        "image": "Naproxen.webp",
        "type": "Anti-Inflamasi (obat radang)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Sakit kepala, nyeri, batuk, demam, sulit berpanas, gangguan pencernaan.",
        "description": "Naproxen adalah obat antiinflamasi nonsteroid (NSAID) yang digunakan untuk mengobati rasa sakit, kram menstruasi, penyakit radang seperti rheumatoid arthritis, dan demam.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/alif-500-mg-10-kaplet"
    },
    "Diklofenak": {
        "image": "Diklofenak.webp",
        "type": "Anti-Inflamasi (obat radang)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Alergi, ruam, sesak napas.",
        "description": "Diklofenak termasuk Obat Anti-Inflamasi Non-Steroid (OAINS) yang digunakan untuk menghilangkan rasa sakit, mulai dari nyeri ringan hingga sedang. Obat ini bekerja dengan cara mengurangi zat dalam tubuh yang menyebabkan rasa sakit dan peradangan.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/natrium-diklofenak-50-mg-10-tablet"
    },
    "Clonidine": {
        "image": "clonidine.jpeg",
        "type": "Anti-Hipertensi",
        "category": "Obat dengan resep dokter",
        "side_effects": "Sakit kepala, mulut kering, sembelit, mual serta insomnia.",
        "description": "Azithromycin adalah obat yang digunakan untuk meredakan tekanan darah tinggi.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/clonidine-0-15-mg-10-tablet"
    },
    "Amlodipine": {
        "image": "Benazepril.jpg",
        "type": "Anti-Hipertensi (Tekanan darah tinggi)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Rasa kantuk, pusing, batuk, sakit kepala, mual.",
        "description": "Benazepril adalah obat untuk menangani hipertensi (tekanan darah tinggi). Dengan terkontrolnya tekanan darah, risiko terjadinya komplikasi, seperti gagal jantung, gagal ginjal, serangan jantung, atau stroke, bisa diturunkan.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/amlodipine-10-mg-10-tablet"
    },
    "Perindopril": {
        "image": "Perindopril.jpeg",
        "type": "Anti-Hipertensi (Tekanan darah tinggi)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Batuk kering, sakit kepala, penglihatan buram, pusing, diare, muntah.",
        "description": "Perindopril adalah obat untuk menurunkan tekanan darah pada penderita hipertensi(tekanan darah tinggi). Tekanan darah yang terkontrol dapat menurunkan risiko terjadinya komplikasi, termasuk gagal fungsi ginjal, stroke, atau serangan jantung. Obat ini juga digunakan dalam pengobatan gagal jantung. ",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/bioprexum-5-mg-30-tablet"
    },
    "Olanzapine": {
        "image": "Olanzapine.webp",
        "type": "Antipsikotik (Gangguan jiwa)",
        "category": "Obat bebas",
        "side_effects": "Pusing, kantuk, dispepsia.",
        "description": "Olanzapine merupakan obat antipsikotik yang digunakan untuk mengobati kondisi psikotik (gangguan jiwa) seperti skizofrenia dan gangguan bipolar (manik depresi ).",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/zyprexa-10-mg-tablet"
    },
"Asenapine": {
        "image": "Asenapine.jpg",
        "type": "Antipsikotik (Gangguan jiwa)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Penglihatan kabur, pusing, sakit kepala, kegugupan, berdebar-debar di telinga, detak jantung lambat atau cepat.",
        "description": "Asenapine adalah obat antipsikotik(gangguan jiwa). Asenapine membantu meringankan gejala yang umum pada skizofrenia, seperti pikiran yang menyimpang dan ketidakstabilan emosional..",
        "buy_link": "-"
    },
    "Paliperidone": {
        "image": "Paliperidone.jpg",
        "type": "Antipsikotik (Gangguan jiwa)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Kesulitan berbicara, detak jantung cepat atau tidak teratur, kehilangan kendali keseimbangan.",
        "description": "Paliperidone adalah agen antipsikotik (gangguan jiwa) generasi kedua (atipikal) yang tersedia dalam bentuk parenteral kerja oral dan panjang dan digunakan dalam pengobatan skizofrenia.",
        "buy_link": "-"
    },
    "Acyclovir": {
        "image": "Acyclovir.jpeg",
        "type": "Antivirus (Infeksi virus)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Lesu, mual, muntah, sakit perut, pusing.",
        "description": "Acyclovir adalah obat antivirus generik dengan kandungan Acyclovir yang digunakan untuk mengobati infeksi akibat virus seperti pengobatan infeksi herpes simpleks pada kulit & membran mukosa, termasuk herpes genital awal & rekuren. Pencegahan infeksi herpes simpleks berulang pada pasien imunokompeten.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/acyclovir-400-mg-10-tablet"
    },
    "Methisoprinol": {
        "image": "Methisoprinol.jpeg",
        "type": "Antivirus (Infeksi virus)",
        "category": "Obat bebas",
        "side_effects": "Efek samping gastrointestinal dan sistem saraf.",
        "description": "Methisoprinol merupakan turunan purin dengan sifa antivirus dan imunomodulator. Obat ini digunakan sebagai Imunomodulator pada infeksi virus & untuk kondisi sistem imun/daya tahan tubuh yang kurang baik, dengan cara merangsang fungsi sel limfosit T dan makrofag dan mempengaruhi produksi sitokin, sehingga menormalkan kekebalan tubuh yang dimediasi sel yang disfungsional.",
        "buy_link": "https://www.onlinepharmacy.com/azithromycin"
    },
    "Atenolol": {
        "image": "Atenolol.webp",
        "type": "Beta blocker (Tekanan darah)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Sesak napas dan pergelangan kaki membengkak.",
        "description": "Atenolol adalah obat yang digunakan untuk mengobati tekanan darah tinggi. Ini juga mencegah nyeri dada (angina) atau serangan jantung..",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/farnormin-50-mg-10-tablet"
    },
    "Betaxolol": {
        "image": "Betaxolol.webp",
        "type": "Beta blocker (Tekanan darah)",
        "category": "Obat bebas",
        "side_effects": "Nyeri dan rasa tidak nyaman.",
        "description": "Betaxolol adalah obat  yang digunakan untuk mengobati peningkatan tekanan darah pada mata yang disebabkan oleh glaukoma sudut terbuka atau suatu kondisi yang disebut hipertensi okular (mata).",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/optibet-eye-drops-5-ml"
    },
    "Bisoprolol": {
        "image": "bisoprolol.webp",
        "type": "Beta blocker (Tekanan darah)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Menyebabkan iritasi.",
        "description": "Bisoprolol adalah obat yang digunakan untuk mengobati tekanan darah tinggi hipertensi dan serangan jantung.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/bisoprolol-5-mg-10-tablet"
    },
    "Terbutaline": {
        "image": "Terbutaline.webp",
        "type": "Antiasthmatic (Obat asma atau sesak)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Gemetar di tungkai, lengan, tangan atau kaki.",
        "description": "Terbutaline digunakan untuk mengobati mengi dan juga sesak nafas yang di akibatkan karena paru-paru. Obat ini tergolong obat bronkodilator yang bekerja dengan cara melemaskan bagian otot di sekitar saluran udara sehingga dapat terbuka dan bernapas dengan lebih mudah.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/nairet-2-5-mg-10-tablet"
    },
    "Isosorbide": {
        "image": "Isosorbide.webp",
        "type": "Antiasthmatic (Obat asma atau sesak)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Sakit kepala, insomnia, berkeringat, mual, muntah, diare, ruam kulit.",
        "description": "Isosorbide dinitrate adalah obat yang digunakan untuk mencegah dan mengobati angina (nyeri dada/sesak) pada penderita masalah jantung tertentu, seperti penyakit jantung koroner (PJK) dan gagal jantung kongestif.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/isosorbide-dinitrate-10-mg-10-tablet"
    },
    "Epinefrin": {
        "image": "Epinefrin.jpg",
        "type": "Antiasthmatic (Obat asma atau sesak)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Sakit kepala, pusing, masalah pada sistem pernapasan, detak jantung berpacu cepat, timbul perasaan cemas atau takut.",
        "description": "Epinefrin adalah obat yang digunakan pada situasi alergi berat seperti sesak yang terjadi akibat gigitan serangga, makanan, obat-obatan, dll. Epinefrin akan dengan cepat membantu melebarkan saluran napas, menstimulasi jantung, meningkatkan tekanan darah, dan menurunkan bengkak pada wajah, bibir, atau tenggorokan.",
        "buy_link": "-"
    },
    "Procaterol": {
        "image": "Procaterol.webp",
        "type": "Antiasthmatic (Obat asma atau sesak)",
        "category": "Obat bebas",
        "side_effects": "Sakit kepala dan kantuk.",
        "description": "Procaterol adalah obat yang digunakan untuk mengatasi sesak napas.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/ataroc-25-mcg-10-tablet"
    },
    "Budesonide": {
        "image": "Budesonide.webp",
        "type": "Kortikosteroid",
        "category": "Obat dengan resep dokter",
        "side_effects": "Tenggorokan kering, sakit kepala, mual, muntah, diare, iritasi pada hidung, mudah lelah.",
        "description": "Budesonide adalah obat kelas kortikosteroid, dengan aktivitas glukokortikoid yang poten. Obat ini mengatur kecepatan sintesis protein, menghambat migrasi sel-sel imun tertentu yang menyebabkan peradangan, mengatur permeabilitas pembuluh kapiler dan stabilitas lisosom, sehingga mencegah dan mengatasi peradangan. .",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/pulmicort-0-5-mg-ml-5-respules"
    },
    "Bethamethason": {
        "image": "Bethamethason.webp",
        "type": "Kortikosteroid (Obat peradangan)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Sakit kepala, sulit tidur, kelenjar keringat berlebih.",
        "description": "Bethamethason adalah obat yang digunakan untuk untuk meredakan gejala peradangan pada sejumlah kondisi, seperti alergi, radang sendi, lupus, sarkoidosis, kolitis ulseratif, atau asma.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/betamethasone-0-1-cream-5-g"
    },
    "Dexamethasone": {
        "image": "Dexamethasone.png",
        "type": "Kortikosteroid (Obat peradangan)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Pusing, penglihatan kabur, sakit kepala, perubahan mood, setak jantung tidak teratur, kesulitan bernapas.",
        "description": "Dexamethasone adalah kortikosteroid yang digunakan untuk mengobati peradangan seperti alergi dan kondisi kulit.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/dexamethasone-0-5-mg-10-tablet"
    },
    "Pseudoephedrine": {
        "image": "Pseudoephedrine.webp",
        "type": "Dekongestan (Hidung tersumbat)",
        "category": "Obat dengan resep dokter",
        "side_effects": "Mual, muntah,sakit kepala, pusing, gelisahatau gugup, sulit tidur.",
        "description": "Pseudoephedrine merupakan dekongestan. Obat ini bekerja dengan cara mengurangi pembengkakan pembuluh darah di rongga hidung. Dengan begitu, penderita hidung tersumbat dapat bernapas lebih lega..",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/tremenza-10-tablet"
    },
    "Guaifenesin": {
        "image": "Guaifenesin.jpg",
        "type": "Ekspektoran (Saluran pernafasan)",
        "category": "Obat bebas",
        "side_effects": "Rasa kantuk, pusing, sakit kepala, nyeri pada perut, mual atau muntah, ruam pada kulit.",
        "description": "Guaifenesin adalah obat generik yang berfungsi sebagai ekspektoran dimana berguna untuk melegakan tenggorokan dan dada yang disebabkan oleh batuk, infeksi, atau alergi.",
        "buy_link": "https://www.halodoc.com/obat-dan-vitamin/guaifenesin-glyceryl-guaiacolate-gg-100-mg-10-tablet"
        }
}

# Create Streamlit app
def absolute_value(x):
    return (x**2) ** 0.5

# Create sidebar option
with st.sidebar:
    selected_option = option_menu("MedBase", options=["Home Page","About MedBase", "Our Profile"], icons=["house-door","exclamation-circle", "person-raised-hand"])

    # Create Home Page
if selected_option == 'Home Page':
   
    # Create a title 
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>Database Obat-Obatan Umum⚕️</h1>", unsafe_allow_html=True)
    
    # Create a search bar
    search_query = st.text_input("Cari obat yang dibutuhkan")
    
    # Filter the medicine data based on the search query
    filtered_medicines = {name: info for name, info in medicines.items() if search_query.lower() in name.lower() or search_query.lower() in info["description"].lower()}
    
    # Create a grid of medicine pictures and descriptions
    num_cols = 4
    if filtered_medicines:
        for i in range(0, len(filtered_medicines), num_cols):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                if i + j < len(filtered_medicines):
                    medicine_name = list(filtered_medicines.keys())[i + j]
                    image_path = filtered_medicines[medicine_name]["image"]
                    image = Image.open(image_path)
                    cols[j].image(image, caption=medicine_name, use_column_width=True)
                    cols[j].markdown(f"**Tipe:** {filtered_medicines[medicine_name]['type']}")
                    cols[j].markdown(f"**Golongan:** {filtered_medicines[medicine_name]['category']}")
                    cols[j].markdown(f"**Efek Samping:** {filtered_medicines[medicine_name]['side_effects']}")
                    cols[j].markdown(filtered_medicines[medicine_name]["description"])
                    cols[j].markdown(f"[Beli {medicine_name}]({filtered_medicines[medicine_name]['buy_link']})")
    else:
        # Show the medicine catalog if no filters are selected
        st.write("Menampilakan semua produk:")
        num_cols = 4
        for i in range(0, len(medicines), num_cols):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                if i + j < len(medicines):
                    medicine_name = list(medicines.keys())[i + j]
                    image_path = medicines[medicine_name]["image"]
                    image = Image.open(image_path)
                    cols[j].image(image, caption=medicine_name, use_column_width=True)
                    cols[j].markdown(f"**Tipe:** {medicines[medicine_name]['type']}")
                    cols[j].markdown(f"**Golongan:** {medicines[medicine_name]['category']}")
                    cols[j].markdown(f"**Efek Samping:** {medicines[medicine_name]['side_effects']}")
                    cols[j].markdown(medicines[medicine_name]["description"])
                    cols[j].markdown(f"[Beli {medicine_name}]({medicines[medicine_name]['buy_link']})")

# Create About MedBase Page
elif selected_option == 'About MedBase':
        st.header('𐙚MedBase Profile꒱')
        st.subheader("**Deskripsi MedBase**")
        text = """
        MedBase adalah website yang dibuat menggunakan bahasa pemograman berupa python dan di deploy menggunakan aplikasi streamlit. MedBase merupakan sekumpulan tentang data berupa obat-obatan dengan klasifikasi Medis serta artinya untuk masyarakat awam lebih memahami. Di rangkum dengan secara menarik berupa visual gambaran tentang produk obat tersebut dan tautan pembelian online yang memudahkan pengguna. MedBase juga menampilkan pengertian tentang obat tersebut serta efek sampingnya.
        """
       
        # For justified text
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.subheader("**Fungsi MedBase**")
        multiline_text="MedBase dibuat dengan tujuan mempermudah pengguna untuk mencari obat-obatan berdasarkan nama obat atau keluhan yang di alami. Medbase juga menampilkan beberapa informasi tambahan pada obat yang tersedia berupa tipe obat, golongan obat, efek samping, deskripsi obat dan juga tautan ke marketplace terpercaya untuk membeli obat yang diperlukan."
      
        st.write(multiline_text)
        st.subheader("**Cara Pemakaian MedBase**")
        text = """
         ──────────────── ⋆⋅☆⋅⋆ ─────────────────
        1. Klik menu pencarian yang tersedia untuk mencari obat sesuai dengan kebutuhan
        2. Jika ingin mencari jenis obat lain tidak melalui menu pecarian. Anda dapat melakukan pencarian manual dengan meng-scroll kalatog pada halaman utama (Home Page)
        3. Anda dapat memasukan nama obat atau keluhan yang anda alami pada menu pencarian
        4. Tekan 'Enter' dan tunggu beberapa saat, maka obat yang anda butuhkan akan ditampilkan
        """
        
        # For justified text
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.divider()
        text = """
        *Catatan:*
        Website ini hanya menyediakan beberapa jenis obat-obatan yang di jual secara umum di Indonesia
        """
        
        # For justified text
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)

# Create Our Profile Page
elif selected_option == 'Our Profile':
    st.header('⋆˚࿔ Kelompok Kami 𝜗𝜚˚⋆')
    picture = Image.open('Medbase Teams.jpg')
    st.image(picture, use_column_width=True)
    text = """
    Pepatah mengatakan tak kenal maka tak sayang, maka dari itu perkenalkan kami dari kelompok 1 kelas A, mahasiswa Politeknik AKA Bogor jurusan Analisis Kimia. Terima kasih sudah menggunakan website kami, website ini dibuat dengan harapan dapat berguna sebaik mungkin untuk para penggunanya. Ingin tau anggota kelompok kami siapa saja?? Ayo lihat dibawah ini👇👇👇👇👇
    """
    # For justified text
    html_content = f"""
    <div style="text-align: justify;">
        {text}
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    st.subheader("**Anggota :**")
    
    text = """
    ───────────── ⋆⋅☆⋅⋆ ──────────────
    1. Eka Rossa Daratiaz Saputri (2360114)
    2. Evelyn Ainunnisa Cumbina (2360117)
    3. Maria Alexandra Putri Karepoan (2360165)
    4. Siti Salma Fauzia Sopyan (2360265)
    5. Vany Alfisya Rinaldi (2360284)
    """
     # For justified text
    html_content = f"""
    <div style="text-align: justify;">
        {text}
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)