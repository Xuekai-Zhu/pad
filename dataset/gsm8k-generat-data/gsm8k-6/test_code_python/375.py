def solution():
    # Calculate the wholesale price of the pair of pants
    retail_price = 36
    markup = 0.8
    wholesale_price = retail_price / (1 + markup)
    result = wholesale_price
    return result

print(solution())