a = 20
b = 21
c = 22

if a%2 == 0:
    deska = int(a/2)
elif a%2 != 0:
    deska = int(a/2)+1

if b%2 == 0:
    deskb = int(b/2)
elif b%2 != 0:
    deskb = int(b/2)+1

if c%2 == 0:
    deskc = int (c/2)
elif c%2 != 0:
    deskc = int(c/2)+1

print(deska + deskb + deskc)

#else did not work why?