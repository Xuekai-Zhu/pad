def solution():
    pancake_price = 4.0
    bacon_price = 2.0
    num_pancakes = 60
    num_bacon = 90

    # Calculate the total revenue from pancake sales
    pancake_revenue = num_pancakes * pancake_price

    # Calculate the total revenue from bacon sales
    bacon_revenue = num_bacon * bacon_price

    # Calculate the total revenue from the fundraiser
    total_revenue = pancake_revenue + bacon_revenue
    result = total_revenue
    return result

print(solution())