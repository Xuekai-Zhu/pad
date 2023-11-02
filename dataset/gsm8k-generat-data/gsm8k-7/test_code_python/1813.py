def solution():
    num_tomatoes = 200
    tomato_price = 1.0

    num_carrots = 350
    carrot_price = 1.5

    # Calculate the total revenue from selling all the tomatoes
    total_tomato_revenue = num_tomatoes * tomato_price

    # Calculate the total revenue from selling all the carrots
    total_carrot_revenue = num_carrots * carrot_price

    # Calculate the total revenue from selling all the produce
    total_revenue = total_tomato_revenue + total_carrot_revenue

    result = total_revenue
    return result

print(solution())