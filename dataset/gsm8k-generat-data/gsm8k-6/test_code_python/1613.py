def solution():
    # Calculate the number of houses that buy something
    houses_buying = 50 * 0.2  # 20% of the houses buy something

    # Calculate the number of houses buying each type of knives
    houses_buying_50 = houses_buying / 2
    houses_buying_150 = houses_buying / 2

    # Calculate the total amount sold in a week
    total_sold = 5 * (houses_buying_50 * 50 + houses_buying_150 * 150)

    result = total_sold
    return result

print(solution())