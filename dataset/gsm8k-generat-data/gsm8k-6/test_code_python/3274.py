def solution():
    # Calculate the total number of days the Bobbit worm was eating fish
    eating_days = 14  # 2 weeks

    # Calculate the total number of fish the Bobbit worm ate
    eaten_fish = 2 * eating_days

    # Calculate the number of fish left in the aquarium when James adds 8 more
    remaining_fish = 60 + 8

    # Calculate the number of fish left after the Bobbit worm's feeding spree
    remaining_fish -= eaten_fish

    result = remaining_fish
    return result

print(solution())