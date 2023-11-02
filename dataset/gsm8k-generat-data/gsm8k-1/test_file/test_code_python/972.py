def solution():
    """Sunny is selling gingerbread and apple pie for a fundraiser. On Saturday, he sold 10 boxes of gingerbread and 4 fewer boxes of apple pie, than on Sunday. On Sunday, he sold 5 more boxes of gingerbread than on Saturday and 15 boxes of apple pie. If the gingerbread cost $6 and the apple pie cost $15, how much did Sunny earn for two days?"""
    sat_gingerbread = 10
    sat_apple = sat_gingerbread - 4
    sun_gingerbread = sat_gingerbread + 5
    sun_apple = 15
    sat_earnings = sat_gingerbread * 6 + sat_apple * 15
    sun_earnings = sun_gingerbread * 6 + sun_apple * 15
    total_earnings = sat_earnings + sun_earnings
    result = total_earnings
    return result

print(solution())