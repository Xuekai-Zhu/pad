def solution():
    num_sold_to_construction = 0.5  # 50% of total lemonade
    num_sold_to_kids = 18
    num_given_to_friends = num_sold_to_kids / 2
    num_drunk_by_hazel = 1

    # Calculate the total number of cups of lemonade made by Hazel
    total_cups = (num_sold_to_construction + 1) * 2 * (num_sold_to_kids + num_given_to_friends + num_drunk_by_hazel)
    result = total_cups
    return result

print(solution())