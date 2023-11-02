def solution():
    """Kris is blowing up balloons for her sister’s party. She has 30 minutes to blow up as many balloons as possible and decides to enlist her brother’s help to increase the number of balloons. Kris can blow up a total of 2 balloon per minute, and her brother works twice as fast. After 15 minutes, her brother doubles his speed and works at this new speed for the remaining 15 minutes. After the 30 minutes, how many balloons, in total, did Kris and her brother blow up?"""
    # Define the number of balloons that Kris can blow up per minute
    KRIS_SPEED = 2

    # Calculate the number of balloons that Kris can blow up in 30 minutes
    kris_balloons = KRIS_SPEED * 30

    # Define the number of balloons that Kris's brother can blow up per minute
    BROTHER_SPEED = KRIS_SPEED * 2

    # Calculate the number of balloons that Kris's brother can blow up in the first 15 minutes
    brother_balloons_1 = BROTHER_SPEED * 15

    # Double the brother's speed for the remaining 15 minutes
    BROTHER_SPEED *= 2

    # Calculate the number of balloons that Kris's brother can blow up in the remaining 15 minutes
    brother_balloons_2 = BROTHER_SPEED * 15

    # Calculate the total number of balloons blown up
    total_balloons = kris_balloons + brother_balloons_1 + brother_balloons_2

    # return the result
    result = total_balloons
    return result

print(solution())