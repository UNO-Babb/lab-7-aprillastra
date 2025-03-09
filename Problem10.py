def sum_of_primes(limit):
    """Returns the sum of all prime numbers below the given limit using the Sieve of Eratosthenes."""

    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False 

    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]: 
            for multiple in range(num * num, limit, num):
                is_prime[multiple] = False 

    return sum(i for i in range(limit) if is_prime[i])

# find the sume of all primes below 2 million 
result = sum_of_primes(2000000)
print("The sum of all primes below two million is:", result)