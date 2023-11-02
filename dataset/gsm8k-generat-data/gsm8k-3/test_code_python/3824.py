def solution():
    """Maria gave a third of her money to her friend Isha, half of what she gave to Florence. If Florence received three times as much money as Maria's cousin Rene, and Rene received $300, how much money did Maria give her three friends?"""
    # Define the amount of money Rene received
    rene_money = 300

    # Calculate the amount of money Florence received
    florence_money = (1/2) * (1/3) * maria_money * 3

    # Calculate the amount of money Isha received
    isha_money = (1/3) * maria_money

    # Calculate the total amount of money Maria gave her friends
    total_money = maria_money - florence_money - isha_money

    # Display the total amount of money Maria gave her friends
    result = total_money
    return result

print(solution())