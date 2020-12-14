result = 1
divisors = []

def get_prime(x, divisors=divisors):
    for i in divisors:
        if x % i == 0:
            return i
    return None

for i in range(2, 21):
    prime = get_prime(i)
    if result % i == 0:
        continue
    elif prime:
        result *= prime
    else:
        result *= i
        divisors.append(i)
        
print(result)
