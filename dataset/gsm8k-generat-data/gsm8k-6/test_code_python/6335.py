def solution():
    total_vegetables = 280  # total number of vegetables
    tomatoes = 3  # number of tomatoes for every 1 cucumber
    c = total_vegetables // (tomatoes + 1)  # calculate number of cucumbers
    result = c
    return result

print(solution())