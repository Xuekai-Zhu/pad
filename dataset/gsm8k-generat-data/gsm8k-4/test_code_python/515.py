def solution():
    """Annie is trying to figure out whether it's safe to drive her truck. For every 3 degrees the temperature drops below 32 degrees, Annie's chances of skidding on ice increase 5%. If she goes into a skid, she has a 40% of regaining control. Otherwise, she'll have a serious accident. If the temperature is 8 degrees, what is the percentage chance of Annie getting into a serious accident if she drives?"""
    # Define the initial chance of skidding on ice
    skid_chance = 0

    # Calculate the additional skid chance based on the temperature
    temperature = 8
    if temperature < 32:
        skid_chance += ((32 - temperature) // 3) * 5

    # Calculate the chance of having a serious accident
    accident_chance = 100 - skid_chance

    # Calculate the final chance of having a serious accident, taking into account the chance of regaining control
    final_chance = accident_chance * 0.6

    # return the result
    result = final_chance
    return result

print(solution())