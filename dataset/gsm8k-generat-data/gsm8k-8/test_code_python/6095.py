def solution():
    # Define the current age of Beau's sons
    sons_current_age = 16

    # Find the sum of their ages from 3 years ago
    sons_3_years_ago_age_sum = (sons_current_age - 3) * 3

    # Find Beau's age from 3 years ago
    beau_3_years_ago_age = sons_3_years_ago_age_sum

    # Calculate Beau's current age
    beau_current_age = beau_3_years_ago_age + 3 * 3

    result = beau_current_age
    return result

print(solution())