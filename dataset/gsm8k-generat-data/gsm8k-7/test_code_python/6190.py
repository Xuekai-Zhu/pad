def solution():
    hours_december = 6.5
    days_december = 31

    hours_january = 8.5
    days_january = 31

    total_hours_december = hours_december * days_december
    total_hours_january = hours_january * days_january

    difference = total_hours_january - total_hours_december
    result = difference
    return result

print(solution())