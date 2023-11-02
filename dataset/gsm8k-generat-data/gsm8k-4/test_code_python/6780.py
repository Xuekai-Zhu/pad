def solution():
    """Chuck can ride the merry-go-round 5 times longer than Dave who can only ride it for 10 minutes before getting sick. Erica can stay on the merry-go-round 30% longer than Chuck before getting sick. How long can Erica stay on the merry-go-round?"""
    # Define Dave's riding time in minutes
    dave_time = 10

    # Calculate Chuck's riding time
    chuck_time = dave_time * 5

    # Calculate Erica's riding time
    erica_time = chuck_time * 1.3

    # return the result
    result = erica_time
    return result

print(solution())