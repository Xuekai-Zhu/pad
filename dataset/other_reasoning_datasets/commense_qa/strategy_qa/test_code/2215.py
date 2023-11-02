def solution():
    # Define that Felix Potvin was an NHL goalie and that there is no goalie position on a dodgeball team
    felix_was_goalie = True
    dodgeball_has_no_goalie_position = True
    # Check if Felix has a position on a dodgeball team
    if felix_was_goalie and dodgeball_has_no_goalie_position:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())