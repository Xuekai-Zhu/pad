def solution():
    """Eliana walked 200 steps for her morning exercise, did some press-ups, then added some 300 more steps to her count for the first day. The next day, she walked twice the number of steps she walked on the first day. And on the third day, Eliana walked an additional 100 steps. What's the total number of steps Eliana walked during these three days?"""
    day1_steps = 200 + 300
    day2_steps = day1_steps * 2
    day3_steps = day2_steps + 100
    total_steps = day1_steps + day2_steps + day3_steps
    result = total_steps
    return result

print(solution())