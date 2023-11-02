def solution():
    """Annie is trying to figure out whether it's safe to drive her truck. For every 3 degrees the temperature drops below 32 degrees, Annie's chances of skidding on ice increase 5%. If she goes into a skid, she has a 40% of regaining control. Otherwise, she'll have a serious accident. If the temperature is 8 degrees, what is the percentage chance of Annie getting into a serious accident if she drives?"""
    temp_drop = 32 - 8
    skid_chance_increase = (temp_drop // 3) * 5
    initial_chance = 0
    for i in range(skid_chance_increase):
        if initial_chance == 0:
            initial_chance = 40
        else:
            initial_chance = initial_chance * 0.6
    serious_accident_chance = 100 - initial_chance
    result = serious_accident_chance
    return result

print(solution())