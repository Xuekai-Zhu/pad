def solution():
    kris_speed = 2
    brother_speed = kris_speed * 2
    first_half_time = 15
    second_half_time = 15

    # Calculate the number of balloons Kris can blow up in the first half
    kris_first_half_balloons = kris_speed * first_half_time

    # Calculate the number of balloons the brother can blow up in the first half
    brother_first_half_balloons = brother_speed * first_half_time

    # Calculate the total number of balloons blown up in the first half
    total_first_half_balloons = kris_first_half_balloons + brother_first_half_balloons

    # Double the brother's speed for the second half
    brother_speed *= 2

    # Calculate the number of balloons the brother can blow up in the second half
    brother_second_half_balloons = brother_speed * second_half_time

    # Calculate the total number of balloons blown up in the second half
    total_second_half_balloons = kris_speed * second_half_time + brother_second_half_balloons

    # Calculate the total number of balloons blown up
    total_balloons = total_first_half_balloons + total_second_half_balloons

    result = total_balloons
    return result

print(solution())