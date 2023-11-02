def solution():
    # Calculate the number of strawberry plants Mark had before giving some to his friend
    current_plants = 20  # current number of strawberry plants
    after_giving = current_plants + 4  # number of plants before giving some to friend
    before_doubling = after_giving / 2 / 2 / 2  # number of plants before tripling in 3 months
    initial_plants = before_doubling * 2 * 2 * 2  # initial number of strawberry plants
    result = initial_plants
    return result

print(solution())