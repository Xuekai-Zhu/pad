def solution():
    distance = 5000  # Jenny lives 5000 feet from her school
    popcorn_per_feet = 1 / 25  # Jenny drops 1 kernel of popcorn for every 25 feet she walks
    total_popcorn = distance * popcorn_per_feet  # Calculate total number of popcorn kernels dropped by Jenny
    eaten_popcorn = total_popcorn * 0.25  # A squirrel eats one-quarter of the popcorn

    # Calculate the remaining number of popcorn kernels
    remaining_popcorn = total_popcorn - eaten_popcorn
    result = remaining_popcorn
    return result

print(solution())