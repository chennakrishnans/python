def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_of_three(a, b, c):
    return lcm(a, lcm(b, c))
def gcd_of_three(a, b, c):
    return gcd(gcd(a, b), c)
a,b,c = map(int, input("Enter three numbers separated by spaces: ").split())
print("LCM:", lcm_of_three(a,b,c))
print("GCD:", gcd_of_three(a,b,c))
