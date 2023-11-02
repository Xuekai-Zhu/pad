def solution():
    starting_amount = 2000
    furniture_cost = 400
    rest_amount = starting_amount - furniture_cost

    friend_share = 3/4 * rest_amount
    emma_left = rest_amount - friend_share
    result = emma_left
    return result

print(solution())