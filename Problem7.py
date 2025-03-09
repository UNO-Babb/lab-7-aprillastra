def isPrime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: 
            return False 
    return True 

def findNthPrime(nth): 
    """Finds the nth prime number."""
    prime_count = 0 
    number = 1 

    while prime_count < nth: 
        number += 1 
        if isprime(number):
            prime_count += 1 

    return number 

# Find the 10001st prime number 
result = findNthPrime(10001)
print("The 10001st prime number is:", result)