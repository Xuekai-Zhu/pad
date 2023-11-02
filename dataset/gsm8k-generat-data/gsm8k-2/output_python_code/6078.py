def solution():
    """Erin put 16 curlers in her hair. One-fourth of the curlers are small pink ones. There are twice as many medium blue curlers as there are pink ones. The rest are large green curlers. How many large green curlers does Erin have in her hair?"""
    total_curlers = 16
    pink_curlers = total_curlers // 4
    blue_curlers = 2 * pink_curlers
    green_curlers = total_curlers - pink_curlers - blue_curlers
    result = green_curlers
    return result

print(solution())