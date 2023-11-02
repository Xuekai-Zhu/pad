def solution():
    """The amount of water passing through a river at one point in time is 4000 gallons. 
    After a day of heavy rain, the amount of water passing through the river doubles at the same point. 
    If the volume of water passing through the river at that point increases by 6000 gallons on the third day, 
    calculate the total amount of water passing through the river at that point."""
    initial_water = 4000
    doubled_water = initial_water * 2
    total_water = doubled_water + 6000
    result = total_water
    return result

print(solution())