def solution():
    """Maya wants to learn how to lift and right now she can only lift a fourth of what America can. America can lift 240 pounds. As Maya grows stronger, she can add 10 more pounds
    to what she previously could lift. America follows this and now she has hit her peak lift at 300 pounds. If Maya reaches her absolute peak and can lift half of what America can lift,
    how many more pounds can Maya lift now than when she started?"""

    # Define America's maximum lift and Maya's initial lift as a fraction of America's
    america_max = 300
    maya_start = america_max / 4

    # Define the increase in Maya's lift each time she grows stronger
    maya_increase = 10

    # Calculate Maya's maximum lift as a fraction of America's
    maya_max = america_max / 2

    # Calculate Maya's current lift
    maya_current = maya_start + ((maya_max - maya_start) / 2)

    # Calculate the difference between Maya's current lift and her starting lift
    increase = maya_current - maya_start

    # Display the increase in Maya's lift
    result = increase
    return result

print(solution())