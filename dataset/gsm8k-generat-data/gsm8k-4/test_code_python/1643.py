def solution():
    """There are four lamps in Valerie's room. All of them are burnt out, so she needs to buy new light bulbs. She needs 3 small light bulbs and 1 large light bulb. She has $60 to spend. If small light bulbs cost $8 and large light bulbs cost $12, how much money will Valerie have left over?"""
    # Define the number and cost of the small and large light bulbs
    small_bulbs_num = 3
    small_bulbs_cost = 8
    large_bulbs_num = 1
    large_bulbs_cost = 12

    # Calculate the total cost of the light bulbs
    total_cost = (small_bulbs_num * small_bulbs_cost) + (large_bulbs_num * large_bulbs_cost)

    # Calculate the amount of money Valerie will have left over
    leftover_money = 60 - total_cost

    result = leftover_money
    return result

print(solution())