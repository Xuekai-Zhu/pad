def solution():
    # Define the regular ticket price
    regular_price = 2000

    # Calculate the discounted price
    discount = 0.3
    discounted_price = regular_price * (1 - discount)

    # Round the final price to two decimal places
    final_price = round(discounted_price, 2)
    result = final_price
    return result

print(solution())