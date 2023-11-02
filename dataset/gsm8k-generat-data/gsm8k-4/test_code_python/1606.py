def solution():
    """Maya wants to learn how to lift and right now she can only lift a fourth of what America can. America can lift 240 pounds.
    As Maya grows stronger, she can add 10 more pounds to what she previously could lift. America follows this and now she has hit
    her peak lift at 300 pounds. If Maya reaches her absolute peak and can lift half of what America can lift, how many more pounds 
    can Maya lift now than when she started?"""
    # Define America's starting lift
    america_starting_lift = 240

    # Define Maya's starting lift
    maya_starting_lift = america_starting_lift / 4

    # Define Maya's absolute peak lift
    maya_peak_lift = america_starting_lift / 2

    # Calculate Maya's final lift after adding 10 pounds at a time
    maya_final_lift = maya_starting_lift
    while maya_final_lift < maya_peak_lift:
        maya_final_lift += 10

    # Calculate the difference between Maya's final lift and her starting lift
    lift_difference = maya_final_lift - maya_starting_lift

    result = lift_difference
    return result

print(solution())