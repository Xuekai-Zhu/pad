def solution():
    # Calculate the total amount of goods she sells on a good week
    good_week_sales = 2 * 800

    # Calculate the total amount of goods she sells in 5 good weeks
    total_good_sales = 5 * good_week_sales

    # Calculate the total amount of goods she sells in 3 tough weeks
    total_tough_sales = 3 * 800

    # Calculate the total amount of money she makes
    total_sales = total_good_sales + total_tough_sales
    result = total_sales
    return result

print(solution())