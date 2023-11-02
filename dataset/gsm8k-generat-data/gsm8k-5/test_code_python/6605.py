def solution():
    total_required_hours = 1500  # Rita's swimming coach requires her to swim a total of 1,500 hours
    hours_completed = 50 + 9 + 121  # Rita has already completed 50 hours of backstroke, 9 hours of breaststroke, and 121 hours of butterfly
    hours_required_per_month = 220  # Rita has decided to dedicate 220 hours every month practicing freestyle and sidestroke

    # Calculate the remaining number of hours Rita needs to complete
    hours_remaining = total_required_hours - hours_completed

    # Calculate the number of months Rita needs to fulfill her coach's requirements
    months_required = hours_remaining // hours_required_per_month
    result = months_required
    return result

print(solution())