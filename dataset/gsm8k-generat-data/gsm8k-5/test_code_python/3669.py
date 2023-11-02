def solution():
    # Calculate the number of chocolate-flavored ice creams sold
    chocolates_sold = round(3/5 * 50)

    # Calculate the number of mango-flavored ice creams sold
    mangoes_sold = round(2/3 * 54)

    # Calculate the total ice creams not sold
    total_not_sold = 50 + 54 - chocolates_sold - mangoes_sold
    result = total_not_sold
    return result

print(solution())