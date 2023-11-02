def solution():
    avocados_cost = 2  # Each avocado costs $2
    avocados_total_cost = 3 * avocados_cost  # Calculate the total cost of 3 avocados
    initial_amount = 20  # Lucas had $20

    # Calculate the amount of change Lucas brings home
    change = initial_amount - avocados_total_cost
    result = change
    return result

print(solution())