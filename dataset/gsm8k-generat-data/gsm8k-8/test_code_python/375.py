def solution():
    # Define the retail price and markup percentage
    retail_price = 36
    markup_percentage = 80/100

    # Calculate the wholesale price using the markup formula
    wholesale_price = retail_price / (1 + markup_percentage)

    result = wholesale_price
    return result

print(solution())