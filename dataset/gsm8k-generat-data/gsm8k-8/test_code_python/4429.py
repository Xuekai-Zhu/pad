def solution():
    # Calculate the total amount of water needed by Ivy for 4 days
    total_water = 2.5 * 4

    # Calculate the number of bottles needed by dividing the total water by the capacity of each bottle
    num_bottles = total_water / 2

    # Round up the number of bottles to ensure that Ivy has enough water for 4 days
    num_bottles = math.ceil(num_bottles)

    result = num_bottles
    return result

print(solution())