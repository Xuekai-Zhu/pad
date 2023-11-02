def solution():
    # Calculate the cost of wasted meat in dollars
    meat_cost = 20 * 5

    # Calculate the cost of wasted fruits and vegetables in dollars
    fruits_veg_cost = 15 * 4

    # Calculate the cost of wasted bread products in dollars
    bread_cost = 60 * 1.5

    # Calculate the cost of janitorial staff in dollars
    janitor_cost = 10 * 10 * 1.5

    # Calculate the total cost in dollars
    total_cost = meat_cost + fruits_veg_cost + bread_cost + janitor_cost

    # Calculate the number of hours James needs to work to pay for everything
    hours_to_work = total_cost / 8

    result = hours_to_work
    return result

print(solution())