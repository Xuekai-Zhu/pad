def solution():
    length = 10
    width = 25
    tiles_per_foot = 4
    num_feet = length * width
    num_tiles = num_feet * tiles_per_foot
    percent_green = 40
    percent_red = 100 - percent_green
    num_green_tiles = num_tiles * (percent_green/100)
    num_red_tiles = num_tiles * (percent_red/100)
    price_green = 3
    price_red = 1.50
    cost_green = num_green_tiles * price_green
    cost_red = num_red_tiles * price_red
    total_cost = cost_green + cost_red
    result = total_cost
    
    return result

print(solution())