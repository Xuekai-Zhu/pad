def solution():
    """Jake is from a conservative household so during lunch at school one day, he gave one-quarter of his feeding allowance to a hungry friend. If candies cost 20 cents apiece and Jake's feeding allowance is $4, how many candies can his friend purchase with the money Jake gave to him?"""
    feeding_allowance = 4
    portion_given = feeding_allowance / 4
    cost_per_candy = 0.20
    candies_purchased = int(portion_given / cost_per_candy)
    result = candies_purchased
    return result

print(solution())