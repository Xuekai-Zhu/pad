def solution():
    starting_amount = 0  # Initialize the starting amount of chocolate milk
    breakfast_amount = 8  # Holly drinks 8 ounces of chocolate milk with breakfast
    lunch_amount = 56  # Holly ends the day with 56 ounces of chocolate milk
    dinner_amount = 8  # Holly drinks 8 ounces of chocolate milk with dinner

    # Calculate the total amount of chocolate milk Holly drank during the day
    total_drank = breakfast_amount + lunch_amount + dinner_amount

    # Calculate the starting amount by subtracting the total drank from the ending amount
    starting_amount = lunch_amount + total_drank - lunch_amount
    result = starting_amount
    return result

print(solution())