def solution():
    """Jay is making snowballs to prepare for a snowball fight with his sister. He can build 20 snowballs in an hour, but 2 melt every 15 minutes. How long will it take before he has 60 snowballs?"""
    snowballs_per_hour = 20
    snowballs_needed = 60
    snowballs_melted_per_time = 2
    time_to_melt = 15  # in minutes
    time = 0
    while snowballs_needed > 0:
        time += 1
        if time % (time_to_melt // 5) == 0:
            snowballs_per_hour -= snowballs_melted_per_time
        snowballs_needed -= snowballs_per_hour // 3
    result = time
    return result

print(solution())