def solution():
    # Calculate the cost of wasted meat
    meat_cost = 20 * 5

    # Calculate the cost of wasted fruits and vegetables
    fruit_veggie_cost = 15 * 4

    # Calculate the cost of wasted bread products
    bread_cost = 60 * 1.5

    # Calculate the cost of janitorial staff's overtime pay
    janitorial_cost = 10 * 1.5 * 10

    # Calculate the total cost of all the wasted food and pay
    total_cost = meat_cost + fruit_veggie_cost + bread_cost + janitorial_cost

    # Calculate the number of hours James has to work
    hours_to_work = total_cost / 8

    result = hours_to_work
    return result

print(solution())