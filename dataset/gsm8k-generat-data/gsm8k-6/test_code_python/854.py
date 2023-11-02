def solution():
    # Calculate the total minutes Jeff ran for the week
    weekdays = 5  # number of weekdays in a week
    duration_per_day = 60  # Jeff committed to run for an hour a day
    duration_on_thursday = duration_per_day - 20  # Jeff cut short his run on Thursday by 20 minutes
    duration_on_friday = duration_per_day + 10  # Jeff jogged 10 minutes more on Friday
    total_duration = (duration_per_day * weekdays) - 20 + 10  # subtract 20 minutes from Thursday and add 10 minutes to Friday
    result = total_duration
    return result

print(solution())