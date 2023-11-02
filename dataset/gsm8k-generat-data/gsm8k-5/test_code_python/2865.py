def solution():
    peaches_per_basket = 25  # There were 25 peaches in each basket
    baskets_delivered = 5  # Five baskets of peaches were delivered
    peaches_eaten = 5  # The farmers have eaten 5 peaches
    peaches_remaining = (baskets_delivered * peaches_per_basket) - peaches_eaten  # Calculate the number of peaches remaining

    # Calculate the number of boxes of peaches
    boxes_of_peaches = peaches_remaining // 15

    result = boxes_of_peaches
    return result

print(solution())