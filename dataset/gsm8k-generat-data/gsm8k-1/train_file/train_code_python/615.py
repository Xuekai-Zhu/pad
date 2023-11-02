def solution():
    """Kris is blowing up balloons for her sister’s party. She has 30 minutes to blow up as many balloons as possible and decides to enlist her brother’s help to increase the number of balloons. Kris can blow up a total of 2 balloons per minute, and her brother works twice as fast. After 15 minutes, her brother doubles his speed and works at this new speed for the remaining 15 minutes. After the 30 minutes, how many balloons, in total, did Kris and her brother blow up?"""
    kris_speed = 2
    brother_speed = kris_speed * 2
    total_time = 30
    first_half_time = 15
    second_half_time = 15
    first_half_balloons = kris_speed * first_half_time + brother_speed * first_half_time / 2
    second_half_balloons = kris_speed * second_half_time + brother_speed * second_half_time
    total_balloons = first_half_balloons + second_half_balloons
    result = total_balloons
    return result

print(solution())