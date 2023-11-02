def solution():
    previous_weight = 6.4
    spider_weight = 2.5 * previous_weight
    leg_area = 0.5
    num_legs = 8

    # Calculate the weight per leg
    leg_weight = spider_weight / num_legs

    # Calculate the pressure per leg
    pressure_per_leg = leg_weight / leg_area

    # Convert pressure to ounces per square inch
    ounces_per_square_inch = pressure_per_leg * 0.5787

    result = ounces_per_square_inch
    return result

print(solution())