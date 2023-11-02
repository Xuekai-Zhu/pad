def solution():
    
    kindergartners = 101
    first_graders = 113
    second_graders = 107
    third_graders = 108
    orange_shirt_price = 5.80
    yellow_shirt_price = 5
    blue_shirt_price = 5.60
    green_shirt_price = 5.25
    total_cost = (kindergartners * orange_shirt_price) + (first_graders * yellow_shirt_price) + \
                 (second_graders * blue_shirt_price) + (third_graders * green_shirt_price)
    result = total_cost
    return result

print(solution())