def solution():
    """James and 4 of his friends volunteered to plant flowers. In 2 days, they were able to plant a total of 200 flowers. If each of them planted the same number of flowers, how many flowers did James plant in a day?"""
    total_friends = 4 + 1
    total_flowers = 200
    days = 2
    flowers_per_day = total_flowers / (total_friends * days)
    james_flowers_per_day = flowers_per_day / total_friends
    result = james_flowers_per_day
    return result

print(solution())