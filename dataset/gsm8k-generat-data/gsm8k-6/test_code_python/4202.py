def solution():
    # Calculate the time spent on dipping the cookies in icing and allowing it to harden
    time_for_icing = (15 + 30 + 30) / 60  # converting minutes to hours

    # Calculate the remaining time for making the batter and cooling the cookies
    remaining_time = 2 - time_for_icing

    result = remaining_time
    return result

print(solution())