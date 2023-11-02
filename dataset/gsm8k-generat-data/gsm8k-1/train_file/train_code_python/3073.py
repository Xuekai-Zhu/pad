def solution():
    """Carter has a jar with 20 green M&Ms and 20 red M&Ms. He eats 12 of the green M&Ms, then his sister comes and eats half the red M&Ms and adds 14 yellow M&Ms. If Carter picks an M&M at random now, what is the percentage chance he'll get a green M&M?"""
    green_mms = 20
    red_mms = 20
    eaten_green_mms = 12
    eaten_red_mms = 0
    added_yellow_mms = 14
    remaining_green_mms = green_mms - eaten_green_mms
    remaining_red_mms = red_mms - eaten_red_mms
    remaining_yellow_mms = added_yellow_mms
    total_mms = remaining_green_mms + remaining_red_mms + remaining_yellow_mms
    prob_green_mms = remaining_green_mms / total_mms
    percent_chance = prob_green_mms * 100
    result = percent_chance
    return result

print(solution())