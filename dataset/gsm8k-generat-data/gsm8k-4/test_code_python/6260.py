def solution():
    """Sandra wants to buy some sweets. She saved $10 for this purpose. Her mother gave her an additional $4, and her father twice as much as her mother. One candy costs $0.5, and one jelly bean $0.2. She wants to buy 14 candies and 20 jelly beans. How much money will she be left with after the purchase?"""
    # Define the initial amount of money
    initial_money = 10

    # Define the additional money from Sandra's mother
    mother_money = 4

    # Define the money from Sandra's father
    father_money = mother_money * 2

    # Calculate the total amount of money
    total_money = initial_money + mother_money + father_money

    # Calculate the cost of buying 14 candies and 20 jelly beans
    cost = (14 * 0.5) + (20 * 0.2)

    # Calculate the remaining amount of money
    remaining_money = total_money - cost

    # return the result
    result = remaining_money
    return result

print(solution())