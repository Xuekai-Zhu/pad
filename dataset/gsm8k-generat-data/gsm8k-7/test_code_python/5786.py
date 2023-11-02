def solution():
    num_buttered_popcorn = 12
    num_caramel_popcorn = 10
    alan_buttered_popcorn = 3
    alan_caramel_popcorn = 1

    # Calculate the total number of bags of popcorn Shelby has
    total_popcorn = num_buttered_popcorn + num_caramel_popcorn

    # Subtract the bags of popcorn Alan took
    total_popcorn -= (alan_buttered_popcorn + alan_caramel_popcorn)

    result = total_popcorn
    return result

print(solution())