fayl_nomi = "report.pdf"

if fayl_nomi.endswith('.pdf'):
    print("Fayl turi: pdf")
elif fayl_nomi.endswith('.docx'):
    print("Fayl turi: docx")
elif fayl_nomi.endswith('.txt'):
    print("Fayl turi: txt")
else:
    print("Fayl turi noma'lum")
