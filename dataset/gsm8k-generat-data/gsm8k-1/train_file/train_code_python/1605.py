def solution():
    """Maya wants to learn how to lift and right now she can only lift a fourth of what America can. America can lift 240 pounds. As Maya grows stronger, she can add 10 more pounds to what she previously could lift. America follows this and now she has hit her peak lift at 300 pounds. If Maya reaches her absolute peak and can lift half of what America can lift, how many more pounds can Maya lift now than when she started?"""
    america_lift = 300
    maya_start = america_lift / 4
    maya_peak = america_lift / 2
    weight_increase = (maya_peak - maya_start)
    result = weight_increase
    return result

print(solution())