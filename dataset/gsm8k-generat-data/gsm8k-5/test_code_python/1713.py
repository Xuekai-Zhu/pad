def solution():
    normal_sales = 21122  # The hobby store normally sells 21122 trading cards per month
    june_sales = normal_sales + 3922  # In June, the hobby store sold 3922 more cards than normal
    july_sales = normal_sales  # In July, the hobby store sold the normal number of cards

    # Calculate the total sales for June and July combined
    total_sales = june_sales + july_sales
    result = total_sales
    return result

print(solution())