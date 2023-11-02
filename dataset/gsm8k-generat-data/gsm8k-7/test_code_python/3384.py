def solution():
    num_capsules_per_bottle = 60
    num_servings_per_bottle = num_capsules_per_bottle / 2
    num_days = 180
    num_servings_needed = num_days * 1  # Barry needs 1 serving per day

    # Calculate the total number of bottles needed
    total_bottles_needed = num_servings_needed / num_servings_per_bottle

    # Round up to the nearest whole number, since Barry can't buy fractional bottles
    total_bottles_needed = int(total_bottles_needed + 0.5)

    result = total_bottles_needed
    return result

print(solution())