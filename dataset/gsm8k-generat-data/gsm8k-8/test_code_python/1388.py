def solution():
    # Count the number of spiders
    spiders = 3

    # Count the number of ants
    ants = 12

    # Count the number of ladybugs (before two fly away)
    ladybugs = 8

    # Subtract the number of flying ladybugs from the total
    flying_ladybugs = 2
    remaining_ladybugs = ladybugs - flying_ladybugs

    # Add up the total number of insects
    total_insects = spiders + ants + remaining_ladybugs

    # Return the result
    result = total_insects
    return result

print(solution())