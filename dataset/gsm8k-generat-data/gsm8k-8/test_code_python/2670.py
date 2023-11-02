def solution():
    # Define the number of people counted on the second day
    second_day_count = 500

    # Calculate the number of people counted on the first day
    first_day_count = 2 * second_day_count

    # Calculate the total number of people counted over the two days
    total_count = first_day_count + second_day_count
    result = total_count
    return result

print(solution())