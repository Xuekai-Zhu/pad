def solution():
    """While shopping, Greg spent 300$ on a shirt and shoes. If Greg spent 9 more than twice as much on shoes as he did a shirt, how much did Greg spend on a shirt?"""
    # Define the total amount spent on the shirt and shoes
    total_amount = 300

    # Set up the equation for the amount spent on shoes
    # x = amount spent on shirt
    # 2x + 9 = amount spent on shoes
    # total_amount = x + (2x + 9)
    # total_amount = 3x + 9
    # 3x = total_amount - 9
    # x = (total_amount - 9)/3

    # Calculate the amount spent on the shirt
    shirt_amount = (total_amount - 9) / 3

    # Return the result
    result = shirt_amount
    return result

print(solution())