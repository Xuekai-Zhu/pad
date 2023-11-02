def solution():
    # Calculate the total amount of fertilizer produced by all the horses in one day
    total_fertilizer = 5 * 80  # each horse produces 5 gallons of fertilizer per day

    # Calculate the total amount of fertilizer needed for all the acres
    total_fertilizer_needed = 400 * 20  # each acre needs 400 gallons of fertilizer and there are 20 acres

    # Calculate the number of days it will take Janet to spread the fertilizer on all the acres
    days_to_spread = total_fertilizer_needed // (total_fertilizer * 4) + 1  # Janet can spread fertilizer over 4 acres per day

    result = days_to_spread
    return result

print(solution())