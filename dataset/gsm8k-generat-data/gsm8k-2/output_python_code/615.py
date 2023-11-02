def solution():
    """Kris is blowing u balloons for her sister’s party. She has 30 minutes to blow up as many balloons as possible and decides to enlist her brother’s help to increase the number of balloons. Kris can blow up a total of 2 balloon per minute, and her brother works twice as fast. After 15 minutes, her brother doubles his speed and works at this new speed for the remaining 15 minutes. After the 30 minutes, how many balloons, in total, did Kris and her brother blow up?"""
    
    kris_speed = 2
    brother_speed = kris_speed * 2

    kris_time = 15
    brother_time = 15

    kris_balloons = kris_time * kris_speed
    brother_balloons = brother_time * brother_speed

    total_balloons = kris_balloons + brother_balloons
    result = total_balloons
    return result

print(solution())