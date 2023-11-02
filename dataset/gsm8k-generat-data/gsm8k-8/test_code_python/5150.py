def solution():
    # Define the full price of one racket
    full_price = 60

    # Calculate the half price of one racket
    half_price = full_price / 2

    # Calculate the total cost of two rackets
    total_cost = full_price + half_price

    # Multiply the total cost by two to include the discount
    final_cost = total_cost * 2
    result = final_cost
    return result

print(solution())