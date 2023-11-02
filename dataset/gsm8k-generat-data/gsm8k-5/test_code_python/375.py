def solution():
    retail_price = 36  # The retail price of a pair of pants is $36
    markup_percentage = 80  # The store owner adds 80% to the wholesale price

    # Calculate the wholesale price
    wholesale_price = retail_price / (1 + markup_percentage / 100) 

    result = wholesale_price
    return result

print(solution())