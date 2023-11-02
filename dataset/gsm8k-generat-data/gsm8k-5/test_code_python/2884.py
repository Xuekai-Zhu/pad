def solution():
    brother_weight = 2 * felix_weight 
    brother_lift = 3 * brother_weight 
    felix_lift = 1.5 * felix_weight 

    # Calculate how much Felix can lift off the ground
    felix_lift = (felix_lift / brother_lift) * 600
    result = felix_lift
    return result

print(solution())