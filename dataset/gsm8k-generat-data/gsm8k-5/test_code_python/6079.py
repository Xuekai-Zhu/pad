def solution():
    total_curlers = 16  # Erin put 16 curlers in her hair
    pink_curlers = total_curlers / 4  # One-fourth of the curlers are small pink ones
    blue_curlers = pink_curlers * 2  # There are twice as many medium blue curlers as there are pink ones
    green_curlers = total_curlers - pink_curlers - blue_curlers  # The rest are large green curlers
    result = green_curlers
    return result

print(solution())