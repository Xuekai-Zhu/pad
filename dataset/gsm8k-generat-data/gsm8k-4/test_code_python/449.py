def solution():
    """A spider has eight legs. If a group of spiders has 10 more spiders than half as many legs as a single spider has, what is the total number of spider legs in this group of spiders?"""
    # Define the number of spider legs per spider
    legs_per_spider = 8

    # Calculate the number of spiders in the group
    spiders = (legs_per_spider / 2) + 10

    # Calculate the total number of spider legs in the group
    total_legs = spiders * legs_per_spider

    # return the result
    result = total_legs
    return result

print(solution())