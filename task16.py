yosh = int(input("Yoshingizni kiriting: "))
narx = 100_000
yanginarh = 0
if yosh <= 8 :
    yanginarh = (50000 * 100_000) / 100_000
    
    print(f"sizning shotingiz {yanginarh} so'm boldi ") 
if yosh > 8 and yosh <= 18 :
    yanginarh = (30000 * 100_000) / 100_000
    yanginarh =narx - yanginarh
    print(f"sizning shotingiz {yanginarh} so'm boldi ") 
elif yosh >18:
    print("sizning shotingiz 100_000 so'm ")
    