def solution():
    is_prime = True
    num_gramophones = 5
    # Check if 5 is a prime number
    if num_gramophones > 1:
        for i in range(2, num_gramophones):
            if num_gramophones % i == 0:
                is_prime = False
                break
    else:
        is_prime = False
    if is_prime:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())