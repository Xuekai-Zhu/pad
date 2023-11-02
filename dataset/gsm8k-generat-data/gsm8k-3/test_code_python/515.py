def solution():
    """Annie is trying to figure out whether it's safe to drive her truck. For every 3 degrees the temperature drops below 32 degrees, Annie's chances of skidding on ice increase 5%. If she goes into a skid, she has a 40% of regaining control. Otherwise, she'll have a serious accident. If the temperature is 8 degrees, what is the percentage chance of Annie getting into a serious accident if she drives?"""
    # Calculate the number of degrees below 32 degrees
    temp_diff = 32 - 8
    temp_diff_div_3 = temp_diff // 3

    # Calculate the chance of skidding on ice
    skid_chance = 1 + (temp_diff_div_3 * 0.05)

    # Calculate the chance of having a serious accident
    serious_chance = 0.6 * skid_chance

    # Display the percentage chance of having a serious accident
    result = serious_chance * 100
    return result

print(solution())