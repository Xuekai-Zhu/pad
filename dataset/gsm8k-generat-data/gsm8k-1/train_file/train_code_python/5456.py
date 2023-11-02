def solution():
    """14 less than two times the number of koi fish in the pond is 64. How many koi fish will you find in the pond?"""
    equation = 2*x - 14
    value = 64
    x = (value + 14)/2
    result = x
    return result

print(solution())