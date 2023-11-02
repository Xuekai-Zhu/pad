def solution():
    horses = 25
    feedings_per_day = 2
    pounds_per_feeding = 20
    days = 60
    pounds_per_ton = 2000

    total_pounds = horses * feedings_per_day * pounds_per_feeding * days
    total_tons = total_pounds / pounds_per_ton

    bags_per_ton = 1/0.5 # One half ton bag per every 0.5 tons of food
    total_bags = total_tons * bags_per_ton

    result = total_bags
    return result

print(solution())