# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors

# def calculate_output(factors):
#     result = 1
#     for factor in factors:
#         return result
    
# number = 87492774
# factors = prime_factors(number)
# output = calculate_output(factors)
# print(output)

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break
    return factors

number = int(input("Enter a number: "))
print("Prime factors of", number, "are:", prime_factors(number))