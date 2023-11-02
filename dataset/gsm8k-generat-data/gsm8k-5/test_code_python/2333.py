def solution():
    total_eggs_weight = 6 # Milo needs 6 pounds of eggs
    egg_weight = 1/16 # An egg weighs 1/16 of a pound

    # Calculate the number of eggs needed to reach 6 pounds
    total_eggs = total_eggs_weight / egg_weight

    # Convert the total number of eggs to dozens of eggs
    dozens_of_eggs = total_eggs / 12
    result = dozens_of_eggs
    return result

print(solution())