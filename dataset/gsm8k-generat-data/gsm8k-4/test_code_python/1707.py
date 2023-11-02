def solution():
    """Anais has 30 more toys than Kamari. There are 160 toys altogether. How many toys are there in Kamari's box?"""
    # Define the difference between Anais and Kamari's number of toys
    diff = 30

    # Calculate the total number of toys
    total_toys = 160

    # Calculate the total number of toys that belong to Kamari and Anais
    # We can set up two equations using the total number of toys and the difference between their numbers of toys
    # Let x be the number of toys in Kamari's box
    # Then x + (x+30) = 160
    # Simplifying gives 2x + 30 = 160, or 2x = 130, or x = 65
    kamari_toys = (total_toys - diff) / 2

    # Return the number of toys in Kamari's box
    result = kamari_toys
    return result

print(solution())