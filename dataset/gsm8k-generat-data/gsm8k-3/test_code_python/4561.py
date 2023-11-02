def solution():
    """Eric, Ben, and Jack have some money. Eric has $10 less than Ben, and Ben has $9 less than Jack. If Jack has $26, how much money, in dollars, do all 3 of them have in total?"""
    # Define the amount of money Jack has
    jack_money = 26

    # Calculate the amount of money Ben has
    ben_money = jack_money + 9

    # Calculate the amount of money Eric has
    eric_money = ben_money - 10

    # Calculate the total amount of money they have
    total_money = jack_money + ben_money + eric_money

    # Display the total amount of money they have
    result = total_money
    return result

print(solution())