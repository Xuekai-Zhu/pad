def solution():
    """Maria gave a third of her money to her friend Isha, half of what she gave to Florence. If Florence received three times as much money as Maria's cousin Rene, and Rene received $300, how much money did Maria give her three friends?"""
    # Define the amount Rene received
    rene_received = 300

    # Calculate the amount Florence received
    florence_received = (1/2) * (1/3) * maria_money * 3

    # Calculate the amount Isha received
    isha_received = (1/3) * maria_money

    # Calculate the total amount of money Maria gave to her friends
    total_received = florence_received + isha_received + rene_received

    # Return the result
    result = total_received
    return result

print(solution())