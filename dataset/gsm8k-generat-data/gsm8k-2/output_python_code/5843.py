def solution():
    """There are 3 consecutive odd integers that have a sum of -147. What is the largest number?"""
    sum_of_integers = -147
    middle_integer = sum_of_integers / 3
    largest_integer = middle_integer + 2
    result = largest_integer
    return result

print(solution())