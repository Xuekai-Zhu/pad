def solution():
    america_lift = 300
    maya_lift = america_lift / 2
    maya_initial_lift = america_lift / 4

    # Calculate Maya's final lift after increasing by 10 pounds at a time
    while maya_initial_lift < maya_lift:
        maya_initial_lift += 10

    # Calculate the increase in Mayan's lift from her starting point
    increase = maya_initial_lift - (america_lift / 4)
    result = increase
    return result

print(solution())