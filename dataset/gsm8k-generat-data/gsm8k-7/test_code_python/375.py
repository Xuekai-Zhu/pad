def solution():
    retail_price = 36
    markup_percentage = 0.8  # 80% markup

    # Calculate the wholesale price
    wholesale_price = retail_price / (1 + markup_percentage)

    result = wholesale_price
    return result

print(solution())