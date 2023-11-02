def solution():
    # Calculate the profit for the large posters
    large_profit = (2 * 10) - (2 * 5)  # profit per day for large posters = (selling price per poster * number of posters) - (production cost per poster * number of posters)

    # Calculate the profit for the small posters
    small_profit = (5 - 2) * 6 - (5 - 2) * 3  # profit per day for small posters = ((total number of posters - number of large posters) * selling price per poster) - ((total number of posters - number of large posters) * production cost per poster)

    # Calculate the total profit for the week
    total_profit = (large_profit + small_profit) * 5  # multiply the daily profit by 5 for the 5-day week
    result = total_profit
    return result

print(solution())