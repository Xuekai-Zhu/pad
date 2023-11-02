def solution():
    # Calculate the total cost of the 10 movies in the first box
    box1_cost = 10 * 2

    # Calculate the total cost of the 5 movies in the second box
    box2_cost = 5 * 5

    # Calculate the total number of DVDs Duke bought
    total_dvds = 10 + 5

    # Calculate the total cost of all the DVDs
    total_cost = box1_cost + box2_cost

    # Calculate the average price of each DVD
    average_price = total_cost / total_dvds
    result = average_price
    return result

print(solution())