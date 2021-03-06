from json.tool import main
from base64 import b64decode
import binascii
from this import d

# tìm ước chung lớn nhất của a và b


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

# eculid mở rộng


def ex_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d1, x1, y1 = ex_gcd(b, a % b)
        d, x, y = (d1, y1, x1 - (a//b)*y1)
        return d, x, y

# nghịch đảo của a theo modun n


def mod_inv(a, n):
    (d, x, y) = ex_gcd(a, n)
    b = x % n
    return b

# tính a^b mod n


def modular_exponentiation(a, b, n):
    if b == 0:
        return 1
    if b == 1:
        return a
    r = modular_exponentiation(a, b//2, n)
    r = (r*r) % n
    if b % 2 == 1:
        r = (r*a) % n
    return r

# tìm hàm diffie hellman
# DH(g^x) mode p
# g^x = m mode p


def diffie_hellman(p, m, g):
    for i in range(p-1):
        if(pow(g, i) % p == m):
            print("x = ", i)
            break

# tim các phần tử sinh và số các phần tử sinh Z*n
# n = int(input("Cac phan tu sinh cua :"))


def tim_cac_phan_sinh(n):
    z = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            z.append(i)

    s = []
    for i in z:
        for j in z:
            if modular_exponentiation(i, j, n) == 1:
                if j == len(z):
                    s.append(i)
                break
    print("Cac phan tu sinh cua Z", n, " la :")
    for i in s:
        print(i)
    print("-----")
    print("So phan tu sinh :", len(s))


def find_plaintextRSA(p, q, e, y):
    N = q*p
    phi = (q-1)*(p-1)

    for d in range(phi - 1):
        if(((d*e) % phi) == 1):
            break
    return modular_exponentiation(y, d, N)


def one_time_pad():
    mess = input('Plaintext..: ')
    # s = binascii.hexlify(bytes(mess, 'utf-8'))
    plaintext = mess.encode("utf-8").hex()
    print(plaintext)
    ciphertext = input("Cipher is: ")
    key = hex(int(plaintext, 16) ^ int(ciphertext, 16))
    print("key OPT :", key)

    mess1 = input("Plaint text to encode : ")
    text = mess1.encode("utf-8").hex()
    print("Ciphertext is: ", hex(int(text, 16) ^ int(key, 16)))


def find_signaturalRSA(n, e):
    print("\nThử từng đáp án, nếu ra kết quả m giống với đáp án thì chọn.")
    for i in range(4):
        o = int(input("\nNhập o = "))
        print("m is : ", modular_exponentiation(o, e, n))


def input_pk():
    p = int(input("Nhập p = "))
    g = int(input("Nhập g = "))
    sk = int(input("Nhập sk = "))
    d = sk
    pk = modular_exponentiation(g, d, p)
    return (p, g, d)


def find_signatural_elgamal():
    kE = int(input("Nhập kE = "))
    m = int(input("Nhập m = "))
    (p, g, d) = input_pk()
    r = modular_exponentiation(g, kE, p)
    a = m - d*r
    b = mod_inv(kE, p - 1)
    s = (a * b) % (p - 1)
    return (r, s)


def menu():
    print("")
    print("Menu")
    print("1.Tim uoc chung lon nhat cua hai so.")
    print("2.Tinh eculid mo rong.")
    print("3.Tim a^-1 mode n.")
    print("4.Tính a^b mod n.")
    print("5.Hàm diffie hellman.")
    print("6.Tìm các phần tử sinh của dãy.")
    print("7.Mã hóa RSA, tìm bản rõ x.")
    print("8.Tìm key OTP")
    print("9.Tìm chữ ký RSA")
    print("10.Tìm chữ kí Elgamal")
    print("0.Exit.")
    x = int(input("Choose: "))
    print("")

    if x == 1:
        a = int(input("Nhap a = "))
        b = int(input("Nhap b = "))
        print("gcd(", a, ",", b, ") = ", gcd(a, b))
        menu()
    elif x == 2:
        a = int(input("Nhap a = "))
        b = int(input("Nhap b = "))
        print("ex_gcd(", a, ",", b, ") = ", gcd(a, b))
        menu()
    elif x == 3:
        a = int(input("Nhap a = "))
        n = int(input("Nhap n = "))
        a1 = mod_inv(a, n)
        print(a, "^-1 mode ", n, " = ", a1)
        menu()
    elif x == 4:
        a = int(input("Nhap a = "))
        b = int(input("Nhap b = "))
        n = int(input("Nhap n = "))
        print(a, "^", b, " mode ", n, " = ", modular_exponentiation(a, b, n))
        menu()
    elif x == 5:
        p = int(input("Nhap p = "))
        m = int(input("Nhap m = "))
        g = int(input("Nhap g = "))
        print("x = ", diffie_hellman(p, m, g))
        menu()
    elif x == 6:
        n = int(input("Nhập n = "))
        tim_cac_phan_sinh(n)
        menu()
    elif x == 7:
        p = int(input("Nhập p ="))
        q = int(input("Nhập q ="))
        e = int(input("Nhập e ="))
        y = int(input("Nhập y ="))
        print("Bản rõ là :", find_plaintextRSA(p, q, e, y))
        menu()
    elif x == 8:
        one_time_pad()
        menu()
    elif x == 9:
        n = int(input("Nhập n = "))
        e = int(input("Nhập e = "))
        find_signaturalRSA(n, e)
        menu()
    elif x == 10:
        print("(r,s) : ", find_signatural_elgamal())
        menu()


if __name__ == "__main__":
    menu()
