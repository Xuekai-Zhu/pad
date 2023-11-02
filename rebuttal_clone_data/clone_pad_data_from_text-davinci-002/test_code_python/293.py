def solution():
    """For every 1 minute that Carlotta sings on stage during the final opera performance, she spends an additional 3 minutes practicing and 5 minutes throwing temper tantrums. If her final stage performance is 6 minutes long, what is the total combined amount of time, in minutes, that she spends practicing, throwing tantrums, and singing in the final stage performance?"""
    minutes_carlotta_sings = 6
    minutes_carlotta_practices = minutes_carlotta_sings * 3
    minutes_carlotta_throwing_tantrums = minutes_carlotta_sings * 5
    total_minutes = minutes_carlotta_sings + minutes_carlotta_practices + minutes_carlotta_throwing_tantrums
    result = total_minutes
    return result

print(solution())