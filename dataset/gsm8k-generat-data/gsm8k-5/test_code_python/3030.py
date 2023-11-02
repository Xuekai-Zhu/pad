def solution():
    total_videos = 411  # The friends watched 411 short videos in total

    # Let's use variables to represent the number of videos each friend watched
    # We can set up two equations based on the given information
    # Kelsey = Ekon + 43      (Equation 1)
    # Ekon = Uma - 17         (Equation 2)

    # We can substitute Equation 2 into Equation 1 to get Kelsey in terms of Uma
    # Kelsey = (Uma - 17) + 43
    # Kelsey = Uma + 26

    # Now we have an equation for Kelsey in terms of Uma, and we know the total number of videos
    # We can substitute the new equation for Kelsey into the equation for the total number of videos
    # Total = Kelsey + Ekon + Uma
    # 411 = (Uma + 26) + (Uma - 17) + Uma
    # 411 = 3Uma + 9
    # 3Uma = 402
    # Uma = 134

    # Now we can use Equation 2 to find Ekon
    # Ekon = Uma - 17
    # Ekon = 134 - 17
    # Ekon = 117

    # Finally, we can use Equation 1 to find Kelsey
    # Kelsey = Ekon + 43
    # Kelsey = 117 + 43
    # Kelsey = 160

    result = 160
    return result

print(solution())