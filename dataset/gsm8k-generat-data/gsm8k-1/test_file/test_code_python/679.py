def solution():
    """Chris has a two-speed lawn mower. He can mow his entire lawn in "turtle" mode in 1 hour, or 40 minutes in "rabbit" mode. Today, he experimented by mowing half in turtle mode and half in rabbit mode. How many minutes did it take him to mow the lawn?"""
    turtle_time = 60
    rabbit_time = 40
    total_time = (turtle_time/2) + (rabbit_time/2)
    result = total_time
    return result

print(solution())