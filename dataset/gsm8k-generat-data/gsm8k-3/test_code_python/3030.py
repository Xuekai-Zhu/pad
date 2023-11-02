def solution():
    """Together 3 friends watched 411 short videos. Kelsey watched 43 more than Ekon. Ekon watched 17 less than Uma. How many videos did Kelsey watch?"""
    
    # Set up the equations
    # k + e + u = 411   (together they watched 411 videos)
    # k = e + 43        (Kelsey watched 43 more than Ekon)
    # e = u - 17        (Ekon watched 17 less than Uma)
    
    # Substitute e = u - 17 into k = e + 43
    # k = (u - 17) + 43
    # k = u + 26
    
    # Substitute k = u + 26 into k + e + u = 411
    # (u + 26) + (u - 17) + u = 411
    # 3u + 9 = 411
    # 3u = 402
    # u = 134
    
    # From this we can find that e = 117 and k = 160
    
    # Display the number of videos Kelsey watched
    result = 160
    return result

print(solution())