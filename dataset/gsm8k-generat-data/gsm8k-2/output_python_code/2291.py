def solution():
    """Jake is from a conservative household so during lunch at school one day, he gave one-quarter of his feeding allowance to a hungry friend. If candies cost 20 cents apiece and Jake's feeding allowance is $4, how many candies can his friend purchase with the money Jake gave to him?"""
    jake_allowance = 4
    friend_allowance = jake_allowance / 4
    candy_cost = 0.2
    candies_can_purchase = friend_allowance / candy_cost
    result = candies_can_purchase
    return result

print(solution())