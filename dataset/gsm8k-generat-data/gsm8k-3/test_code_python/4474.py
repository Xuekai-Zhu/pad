def solution():
    """Alison has half as much money as Brittany. Brittany has 4 times as much money as Brooke. Brooke has twice as much money as Kent. If Kent has $1,000, how much money does Alison have?"""
    # Define the amount of money Kent has
    kent_money = 1000

    # Calculate the amount of money Brooke has
    brooke_money = kent_money * 2

    # Calculate the amount of money Brittany has
    brittany_money = brooke_money * 4

    # Calculate the amount of money Alison has
    alison_money = brittany_money / 2

    # Display the amount of money Alison has
    result = alison_money
    return result

print(solution())