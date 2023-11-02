def solution():
    """ Jim has a pail with rocks in it. The average weight of a rock is 1.5 pounds. A local rock collector agrees to pay him $4 for every pound of rocks. If he makes $60 off the sale, how many rocks were in the bucket? """
    rock_weight = 1.5
    price_per_pound = 4
    total_sale = 60
    total_weight = total_sale / price_per_pound 
    num_rocks = total_weight / rock_weight
    result = num_rocks
    return result

print(solution())