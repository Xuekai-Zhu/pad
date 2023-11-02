def solution():
    kris_speed = 2 # Kris can blow up 2 balloons per minute
    brother_speed = 4 # Brother works twice as fast as Kris
    total_time = 30 # Kris has 30 minutes to blow up balloons
    first_half_time = 15 # Brother works at his initial speed for the first 15 minutes
    second_half_time = 15 # Brother doubles his speed and works for the remaining 15 minutes

    # Calculate how many balloons Kris can blow up in 15 minutes
    kris_balloons_first_half = kris_speed * first_half_time

    # Calculate how many balloons brother can blow up in 15 minutes at his initial speed
    brother_balloons_first_half = brother_speed * first_half_time

    # Calculate how many balloons brother can blow up in 15 minutes at his new speed
    brother_new_speed = 2 * brother_speed
    brother_balloons_second_half = brother_new_speed * second_half_time

    # Calculate the total number of balloons blown up by Kris and brother
    total_balloons = kris_balloons_first_half + brother_balloons_first_half + brother_balloons_second_half
    result = total_balloons
    return result

print(solution())