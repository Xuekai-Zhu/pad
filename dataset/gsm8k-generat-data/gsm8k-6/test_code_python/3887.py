def solution():
    # Calculate the average miles per day for the second dog
    total_miles = 70  # the total miles the two dogs walk in a week
    miles_per_day_1 = 2  # the first dog walks 2 miles a day
    miles_per_day_2 = (total_miles - (miles_per_day_1 * 7)) / 7  # calculate the miles per day for the second dog
    result = miles_per_day_2
    return result

print(solution())