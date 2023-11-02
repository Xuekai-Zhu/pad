def solution():
    base_chance = 10  # Chances of making the team start at 10% if 66 inches tall
    additional_chance = 10  # Chances increase by 10% for every additional inch of height
    height = 65 + 3  # Devin starts at 65 inches and grows 3 inches

    # Calculate the total likelihood of making the team based on height
    total_chance = base_chance + (height - 66) * additional_chance

    # Ensure the total chance is not greater than 100%
    total_chance = min(total_chance, 100)

    result = total_chance
    return result

print(solution())