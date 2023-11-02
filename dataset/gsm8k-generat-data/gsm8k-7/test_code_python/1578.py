def solution():
    num_chairs_for_table = 3
    num_chairs_for_cost = 5
    cost_for_chairs = 55
    total_money = 100

    # Calculate the cost of one plastic chair
    cost_for_one_chair = cost_for_chairs / num_chairs_for_cost

    # Calculate the cost of one portable table
    cost_for_table = cost_for_one_chair * num_chairs_for_table

    # Calculate the total cost for one portable table and two chairs
    total_cost_for_table_and_chairs = cost_for_table + (2 * cost_for_one_chair)

    # Calculate the remaining money after the purchase
    remaining_money = total_money - total_cost_for_table_and_chairs
    result = remaining_money
    return result

print(solution())