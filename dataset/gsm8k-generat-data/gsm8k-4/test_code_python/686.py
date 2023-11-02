def solution():
    """Jack and Jill shared the cost of renting a cottage that costs $5 an hour. If they rented it for eight hours, how much did each friend pay?"""
    # Define the cost of renting the cottage and the number of hours rented
    rental_cost = 5
    hours_rented = 8

    # Calculate the total cost of renting the cottage
    total_cost = rental_cost * hours_rented

    # Divide the total cost between Jack and Jill
    each_pay = total_cost / 2

    # return the result
    result = each_pay
    return result

print(solution())