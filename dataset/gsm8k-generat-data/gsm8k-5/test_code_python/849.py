def solution():
    total_balloons = 200  # There are 200 balloons in the hot air balloon
    blown_up_first_half = total_balloons / 5  # 1/5 of the balloons blow up in the first half hour
    remaining_balloons = total_balloons - blown_up_first_half  # Balloons remaining after first half hour
    blown_up_second_hour = 2 * blown_up_first_half  # Twice the number of balloons that have already blown up blow up in the second hour

    # Calculate the total number of balloons blown up after two hours
    total_blown_up = blown_up_first_half + blown_up_second_hour

    # Calculate the number of balloons remaining
    remaining_balloons -= total_blown_up
    result = remaining_balloons
    return result

print(solution())