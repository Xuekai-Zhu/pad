def solution():
    # Calculate the total amount spent by Jude
    total_spent = 130 - 4  # given that Jude got a $4 change
    table_cost = 50  # cost of the table
    plates_cost = 20 * 2  # cost of two sets of plates
    chairs_cost = total_spent - (table_cost + plates_cost)  # cost of three chairs
    each_chair_cost = chairs_cost / 3  # cost of each chair
    result = each_chair_cost
    return result

print(solution())