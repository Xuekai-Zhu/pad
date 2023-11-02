def solution():
    num_dresses = 7
    num_shirts = 4
    total_earnings = 69
    shirt_price = 5

    # Calculate the total earnings from selling shirts
    shirt_earnings = num_shirts * shirt_price

    # Calculate the total earnings from selling dresses
    dress_earnings = total_earnings - shirt_earnings

    # Calculate the price of each dress
    dress_price = dress_earnings / num_dresses
    result = dress_price
    return result

print(solution())