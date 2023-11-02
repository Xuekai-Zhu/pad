def solution():
    # Calculate the total distance walked by the unicorns in meters
    total_distance = 9 * 1000  # 1 kilometer equals 1000 meters
    # Calculate the number of steps taken by the unicorns
    total_steps = total_distance / 3
    # Calculate the total number of flowers that will bloom
    total_flowers = total_steps * 4 * 6  # each unicorn steps on 4 flowers and there are 6 unicorns
    result = total_flowers
    return result

print(solution())