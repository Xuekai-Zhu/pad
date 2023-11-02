def solution():
    """Tom has a quarter as much money as Nataly. Nataly has three times as much money as Raquel. How much money do Tom, Raquel, and Nataly have combined if Raquel has $40?"""
    # Define the amount of money Raquel has
    raquel_money = 40

    # Calculate the amount of money Nataly has
    nataly_money = raquel_money * 3

    # Calculate the amount of money Tom has
    tom_money = nataly_money / 4

    # Calculate the total amount of money
    total_money = raquel_money + nataly_money + tom_money

    # Display the total amount of money
    result = total_money
    return result

print(solution())