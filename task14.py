def fayl_turini_aniqla(fayl_nomi):
    if fayl_nomi.endswith('.pdf'):
        return "Fayl turi: pdf"
    elif fayl_nomi.endswith('.docx'):
        return "Fayl turi: docx"
    elif fayl_nomi.endswith('.txt'):
        return "Fayl turi: txt"
    else:
        return "Fayl turi noma'lum"
fayl = "report.pdf"
natija = fayl_turini_aniqla(fayl)
print(natija)

    