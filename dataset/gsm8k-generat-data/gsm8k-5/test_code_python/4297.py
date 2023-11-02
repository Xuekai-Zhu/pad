def solution():
    # Calculate the total cost of DVDs in the first box
    cost_first_box = 10 * 2  # 10 movies at $2 each

    # Calculate the total cost of DVDs in the second box
    cost_second_box = 5 * 5  # 5 movies at $5 each

    # Calculate the total number of DVDs Duke bought
    total_dvds = 10 + 5

    # Calculate the average price of each DVD
    average_price = (cost_first_box + cost_second_box) / total_dvds
    result = average_price
    return result

print(solution())