def solution():
    num_spiders = 3
    num_ants = 12
    num_ladybugs = 8

    # Subtract the number of ladybugs that flew away
    num_ladybugs -= 2

    # Add up the total number of insects remaining
    total_insects = num_spiders + num_ants + num_ladybugs
    result = total_insects
    return result

print(solution())