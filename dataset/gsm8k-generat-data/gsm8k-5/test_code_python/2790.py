def solution():
    small_bears = 4  # Four small panda bears
    big_bears = 5  # Five bigger panda bears
    total_bears = small_bears + big_bears  # Total number of pandas
    bamboo_small_bears = 25  # Small pandas eat 25 pounds of bamboo
    bamboo_big_bears = 40  # Big pandas eat 40 pounds of bamboo
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total amount of bamboo eaten by all pandas in one day
    total_bamboo = (small_bears * bamboo_small_bears) + (big_bears * bamboo_big_bears)

    # Calculate the total amount of bamboo eaten by all pandas in one week
    total_bamboo_week = total_bamboo * days_per_week

    # Return the total amount of bamboo eaten in a week by all pandas
    result = total_bamboo_week
    return result

print(solution())