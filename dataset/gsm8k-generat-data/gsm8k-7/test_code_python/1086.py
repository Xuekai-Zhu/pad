def solution():
    total_harvest = 245.5
    sold_to_maxwell = 125.5
    sold_to_wilson = 78

    # Calculate the total amount of tomatoes sold
    total_sold = sold_to_maxwell + sold_to_wilson

    # Calculate the amount of tomatoes not sold
    not_sold = total_harvest - total_sold
    result = not_sold
    return result

print(solution())