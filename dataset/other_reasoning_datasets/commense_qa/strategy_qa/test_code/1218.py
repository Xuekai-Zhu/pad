def solution():
    bottom_feeder = True
    feeds_on_bottom_food = True
    eats_other_fish = False
    if bottom_feeder and feeds_on_bottom_food and not eats_other_fish:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())