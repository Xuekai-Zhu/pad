def solution():
    # Calculate total ounces of special dog food needed during first 60 days
    total_ounces_first_60_days = 2 * 60

    # Calculate total ounces of special dog food needed after first 60 days
    total_ounces_after_first_60_days = 4 * (365 - 60)

    # Calculate total ounces of special dog food needed
    total_ounces = total_ounces_first_60_days + total_ounces_after_first_60_days

    # Convert total ounces to pounds
    total_pounds = total_ounces / 16

    # Calculate number of 5-pound bags needed
    num_bags = total_pounds / 5

    # Round up to nearest integer
    num_bags = int(num_bags) + (num_bags % 1 > 0)

    result = num_bags
    return result

print(solution())