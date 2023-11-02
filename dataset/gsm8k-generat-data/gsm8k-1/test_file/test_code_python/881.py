def solution():
    """The Ben and Aggie Burrito Shop makes 125 chimichangas on Tuesdays, 125 chimichangas on Wednesdays and twice as many on Friday. How many chimichangas do they make on those three days?"""
    tues_chimis = 125
    wed_chimis = 125
    fri_chimis = 2 * tues_chimis
    total_chimis = tues_chimis + wed_chimis + fri_chimis
    result = total_chimis
    return result

print(solution())