def solution():
    hours = 3
    rate = 15
    tip_percent = 0.2

    # Calculate the total cost of hiring the singer for 3 hours
    total_cost = hours * rate

    # Calculate the amount of tip
    tip = total_cost * tip_percent

    # Calculate the final amount paid
    final_amount = total_cost + tip
    result = final_amount
    return result

print(solution())