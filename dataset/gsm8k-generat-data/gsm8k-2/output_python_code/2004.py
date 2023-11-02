def solution():
    """Hazel put up a lemonade stand. She sold half her lemonade to a construction crew. She sold 18 cups to kids on bikes. She gave away half that amount to her friends. Then she drank the last cup of lemonade herself. How many cups of lemonade did Hazel make?"""
    total_sold_to_construction = 0.5 * total_lemonade
    remaining_lemonade = total_lemonade - total_sold_to_construction - 18
    given_to_friends = remaining_lemonade / 2
    total_lemonade = given_to_friends + total_sold_to_construction + 18 + 1
    result = total_lemonade
    return result

print(solution())