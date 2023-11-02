def solution():
    """Carter has a jar with 20 green M&Ms and 20 red M&Ms. He eats 12 of the green M&Ms,
    then his sister comes and eats half the red M&Ms and adds 14 yellow M&Ms. 
    If Carter picks an M&M at random now, what is the percentage chance he'll get a green M&M?"""
    total_mms = 42 # 20 green + 20 red + 2 yellow (from his sister's actions)
    green_mms = 8  # 20 green - 12 that Carter ate
    red_mms = 10   # 20 red / 2 (his sister ate half)
    yellow_mms = 24 # 20 + 14 that his sister added
    probability_green = green_mms / total_mms * 100
    result = probability_green
    return result

print(solution())