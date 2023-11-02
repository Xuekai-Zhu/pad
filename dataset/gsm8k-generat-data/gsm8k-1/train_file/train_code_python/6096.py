def solution():
    """John has 25 horses. He feeds each horse twice a day and feeds them 20 pounds of food at each feeding. He buys half ton bags of food. How many of those will he have to buy in 60 days?"""
    horses = 25
    feedings_per_day = 2
    pounds_per_feeding = 20
    total_pounds_per_day = horses * feedings_per_day * pounds_per_feeding
    half_ton_in_pounds = 1000 / 2
    bags_per_day = total_pounds_per_day / half_ton_in_pounds
    total_bags = bags_per_day * 60
    result = total_bags
    return result

print(solution())