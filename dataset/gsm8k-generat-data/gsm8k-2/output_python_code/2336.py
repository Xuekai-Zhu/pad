def solution():
    """The P.T.O. decided to provide shirts for the elementary students for track and field day. Each grade was given a different color. 101 Kindergartners wore orange shirts that cost $5.80 each. 113 first graders wore yellow shirts that cost $5 each. 107 second graders wore blue shirts that cost $5.60 each. 108 third graders wore green shirts that cost $5.25 each. How much did the P.T.O. spend on shirts for field day?"""
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