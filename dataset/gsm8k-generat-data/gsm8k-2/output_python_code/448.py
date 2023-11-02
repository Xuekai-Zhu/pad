def solution():
    """A spider has eight legs. If a group of spiders has 10 more spiders than half as many legs as a single spider has, what is the total number of spider legs in this group of spiders?"""
    legs_per_spider = 8
    spiders = (legs_per_spider / 2) + 10
    total_legs = legs_per_spider * spiders
    result = total_legs
    return result

print(solution())