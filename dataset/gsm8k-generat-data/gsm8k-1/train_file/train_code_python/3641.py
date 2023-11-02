def solution():
    """In the matrix, there are seven fewer noodles than pirates. If there are 45 pirates, how many noodles and pirates are there in total?"""
    num_pirates = 45
    num_noodles = num_pirates - 7
    total = num_pirates + num_noodles
    result = total
    return result

print(solution())