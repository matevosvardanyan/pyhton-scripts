
import random

for i in range(800000):
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
#    d = random.randint(0, 255)
    print(f"ip route add {a}.{b}.{c}.0/24 via 10.100.0.25")

