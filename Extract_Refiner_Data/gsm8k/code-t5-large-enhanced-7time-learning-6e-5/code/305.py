def solution():
    
    # Define the number of extra arms and extra leges grown every 3 days
    ARM_GROWTH = 3
    LEG_GROWTH = 5

    # Define the number of days the serum will grow from drinking
    drinking_days = 15

    # Calculate the number of extra arms and leges that will grow
    extra_arms = drinking_days // 3
    extra_legs = drinking_days // LEG_GROWTH

    # Calculate the total number of limbs that will grow
    total_limbs = (extra_arms * ARM_GROWTH) + (extra_legs * LEG_GROWTH)

    # Display the total number of limbs
    result = total_limbs
    return result

print(solution())