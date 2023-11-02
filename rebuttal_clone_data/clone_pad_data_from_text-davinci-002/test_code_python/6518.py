def solution():
    pairs_of_pants_per_year = 4
    pants_per_pair = 2
    initial_pants = 50
    total_pants = initial_pants + (pairs_of_pants_per_year * pants_per_pair * 5)
    result = total_pants
    return result

print(solution())