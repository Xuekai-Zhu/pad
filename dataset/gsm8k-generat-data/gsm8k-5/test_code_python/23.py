def solution():
    shorts_cost = 7  # Each pair of shorts costs $7
    shoes_cost = 10  # Each pair of shoes costs $10
    total_spent = 75  # Ann spent $75 in total
    num_shorts = 5  # Ann bought 5 pairs of shorts
    num_shoes = 2  # Ann bought 2 pairs of shoes

    # Calculate the cost of the tops
    total_cost = total_spent - (num_shorts * shorts_cost) - (num_shoes * shoes_cost)
    num_tops = 4  # Ann bought 4 tops
    top_cost = total_cost / num_tops  # Divide the remaining cost by the number of tops

    result = top_cost
    return result

print(solution())