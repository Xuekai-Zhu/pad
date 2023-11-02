def solution():
    extra_arms_per_day = 3  # The serum will grow an extra arm every 3 days
    extra_leg_per_day = 5  # The serum will grow an extra leg every 5 days
    days_drunk = 15  # The serum will grow for 15 days

    # Calculate the total extra limbs the serum will grow in 15 days
    total_extra_limbs = (extra_arms_per_day * days_drunk) + (extra_leg_per_day * days_drunk)

    # Calculate the new limbs the serum will cause a person to grow
    new_limbs = total_extra_limbs
    result = new_limbs
    return result

print(solution())