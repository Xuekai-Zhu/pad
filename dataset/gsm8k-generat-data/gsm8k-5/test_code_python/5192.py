def solution():
    # Calculate the amounts spent on beef, fruits and vegetables, spices, and other groceries
    beef_cost = 3 * 11
    fruits_cost = 8 * 4
    spices_cost = 3 * 6
    other_cost = 37

    # Calculate the total amount spent and the total points earned
    total_cost = beef_cost + fruits_cost + spices_cost + other_cost
    total_points = (total_cost // 10) * 50

    # Add the bonus points if the total spent is more than $100
    if total_cost > 100:
        total_points += 250

    result = total_points
    return result

print(solution())