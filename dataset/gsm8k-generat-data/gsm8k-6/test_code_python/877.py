def solution():
    # Calculate the number of strawberries Kimberly's brother picked
    brother_strawberries = 3 * 15  

    # Calculate the number of strawberries Kimberly's parents picked
    parent_strawberries = 8 * brother_strawberries - 93  

    # Calculate the total number of strawberries picked
    total_strawberries = brother_strawberries + parent_strawberries + 8 * brother_strawberries  

    # Calculate the number of strawberries each person gets when divided equally
    strawberries_per_person = total_strawberries / 4  

    result = strawberries_per_person
    return result

print(solution())