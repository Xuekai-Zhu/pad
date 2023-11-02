def solution():
    # Calculate the total amount spent on beef
    beef_cost = 11 * 3

    # Calculate the total amount spent on fruits and vegetables
    fv_cost = 8 * 4

    # Calculate the total amount spent on spices
    spice_cost = 6 * 3

    # Calculate the total amount spent on all groceries
    total_cost = beef_cost + fv_cost + spice_cost + 37

    # Calculate the number of prize points earned from spending
    points_from_spending = int(total_cost/10) * 50

    # Calculate the bonus points if Martha spent more than $100
    bonus_points = 250 if total_cost > 100 else 0

    # Calculate the total number of points earned
    total_points = points_from_spending + bonus_points
    result = total_points
    return result

print(solution())