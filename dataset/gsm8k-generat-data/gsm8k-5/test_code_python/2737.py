def solution():
    # Calculate the total cost of tickets for Monday's group
    monday_children = 7
    monday_adults = 5
    monday_cost = (monday_children * 3) + (monday_adults * 4)

    # Calculate the total cost of tickets for Tuesday's group
    tuesday_children = 4
    tuesday_adults = 2
    tuesday_cost = (tuesday_children * 3) + (tuesday_adults * 4)

    # Calculate the total money the zoo made for both days
    total_money = monday_cost + tuesday_cost
    result = total_money
    return result

print(solution())