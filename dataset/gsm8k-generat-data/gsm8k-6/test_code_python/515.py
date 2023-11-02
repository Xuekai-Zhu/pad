def solution():
    # Calculate the percentage chance of skidding on ice
    degrees_below_32 = 32 - 8  # calculate how many degrees below 32 it is
    skid_increase_percent = (degrees_below_32 // 3) * 5  # calculate the percentage increase in skid chance
    skid_chance = 20 + skid_increase_percent  # add the base skid chance to the increase
    no_skid_chance = 100 - skid_chance  # calculate the percentage chance of not skidding

    # Calculate the percentage chance of a serious accident
    serious_accident_chance = no_skid_chance * 60 / 100  # calculate the chance of having a serious accident if there is no skid
    serious_accident_chance += skid_chance * 60 / 100 * 40 / 100  # calculate the chance of having a serious accident if there is a skid

    result = serious_accident_chance
    return result

print(solution())