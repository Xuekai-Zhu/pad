def solution():
    # Define the cost per scoop
    cost_per_scoop = 2

    # Define the number of scoops for each person
    pierre_scoops = 3
    mom_scoops = 4

    # Calculate the total bill
    total_bill = cost_per_scoop * (pierre_scoops + mom_scoops)
    result = total_bill
    return result

print(solution())