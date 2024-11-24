def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    t = 3
    for t in range(3, number // 2, 2):
        if number % t == 0:
            return False
    return True

# def is_even(number):
#     return number % 2 == 0 

# print(is_prime(1))
# print(is_prime(8))
# print(is_prime(13))
# print(is_prime(2))
l = [6363107417]
k = 0
for f in l:
     if is_prime(f):
          k += 1
print(k)