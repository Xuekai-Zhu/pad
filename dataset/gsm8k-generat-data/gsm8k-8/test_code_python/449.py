def solution():
    # Define the number of legs on a single spider
    legs_on_single_spider = 8

    # Calculate half as many legs as a single spider has
    half_legs_on_single_spider = legs_on_single_spider / 2

    # Calculate the number of spiders in the group
    spiders_in_group = half_legs_on_single_spider + 10

    # Calculate the total number of spider legs in the group
    total_legs_in_group = spiders_in_group * legs_on_single_spider
    result = total_legs_in_group
    return result

print(solution())