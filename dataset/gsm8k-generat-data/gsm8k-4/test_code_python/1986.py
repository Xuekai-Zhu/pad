def solution():
    """$240 was divided between Kelvin and Samuel. Samuel received 3/4 of the money. From his share, Samuel then spent 1/5 of the original $240 on drinks. How much does Samuel have left?"""
    # Define the total amount of money
    total_money = 240

    # Calculate Samuel's share
    samuel_share = total_money * 3 / 4

    # Calculate the amount Samuel spent on drinks
    samuel_drinks = samuel_share * 1 / 5

    # Calculate how much Samuel has left
    samuel_left = samuel_share - samuel_drinks

    # return the result
    result = samuel_left
    return result

print(solution())