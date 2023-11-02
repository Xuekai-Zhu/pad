def solution():
    # Calculate the number of houses that buy something
    houses_buying = 0.2 * 50

    # Calculate the number of houses buying each set of knives
    houses_buying_50_knives = 0.5 * houses_buying
    houses_buying_150_knives= 0.5 * houses_buying

    # Calculate the total amount sold
    total_sales = (houses_buying_50_knives * 50) + (houses_buying_150_knives * 150)

    # Calculate the total sales in a week
    weekly_sales = total_sales * 5

    result = weekly_sales
    return result

print(solution())