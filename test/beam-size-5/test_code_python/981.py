def solution():
    
    # Define the number of pretzels Edgar eats per day
    edgar_pretzels_per_day = 18

    # Calculate the number of pretzels his brother eats per day
    brother_pretzels_per_day = edgar_pretzels_per_day / 2

    # Calculate the number of pretzels his brother eats in a week
    brother_pretzels_per_week = brother_pretzels_per_day * 7

    # Display the number of pretzels his brother eats in a week
    result = brother_pretzels_per_week
    return result

print(solution())