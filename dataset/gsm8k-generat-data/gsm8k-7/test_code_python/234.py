def solution():
    bread_cost = 4.20
    cheese_cost = 2.05
    total_cost = bread_cost + cheese_cost
    payment = 7.00
    change = payment - total_cost

    # Calculate the number of quarters in change
    num_quarters = change // 0.25
    change -= num_quarters * 0.25

    # Calculate the number of dimes in change
    num_dimes = change // 0.10
    change -= num_dimes * 0.10

    # Calculate the number of nickels in change
    num_nickels = change // 0.05

    result = num_nickels
    return result

print(solution())