def solution():
    superhero_speed = 10/4  # miles per minute
    supervillain_speed = 100/60  # miles per minute

    # Calculate how many miles farther the superhero can run than the supervillain can drive in one minute
    difference_per_minute = superhero_speed - supervillain_speed

    # Calculate how many miles farther the superhero can run than the supervillain can drive in one hour
    difference_per_hour = difference_per_minute * 60

    result = difference_per_hour
    return result

print(solution())