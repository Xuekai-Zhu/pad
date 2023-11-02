def solution():
    # Find the reduced rate of pumping due to drought restrictions
    reduced_rate = 2/3 * 6  # 2/3rds as fast as normal pumping rate

    # Calculate the time it takes to fill the pond with reduced pumping rate
    time = 200 / reduced_rate  # gallons of water divided by reduced pumping rate in gallons per minute

    result = time
    return result

print(solution())