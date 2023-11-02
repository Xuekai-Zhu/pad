def solution():
    
    feeding_allowance = 4
    portion_given = feeding_allowance / 4
    cost_per_candy = 0.20
    candies_purchased = int(portion_given / cost_per_candy)
    result = candies_purchased
    return result

print(solution())