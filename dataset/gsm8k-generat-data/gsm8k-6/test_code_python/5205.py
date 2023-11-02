def solution():
    total_miles = 26  # total miles in the marathon
    initial_pace = 10  # the pace at which he runs the first 10 miles
    remaining_miles = total_miles - initial_pace  # remaining miles to be covered
    remaining_pace = 0.8 * initial_pace  # pace at which he runs the remaining miles

    # Calculate the total time taken to run the marathon
    time_taken = (initial_pace/10)*60 + (remaining_miles/remaining_pace)*60  # converting the pace to minutes per mile
    result = time_taken
    return result

print(solution())