def solution():
    """Daragh had 20 stuffed bears. She took out her favorite 8 bears and then equally divided the other bears among her 3 sisters. Daragh's youngest sister, Eden, already had 10 stuffed bears. How many stuffed bears does Eden have now?"""
    total_bears = 20
    daragh_fav = 8
    remaining_bears = total_bears - daragh_fav
    other_sisters_bears = remaining_bears / 3
    eden_bears = other_sisters_bears + 10
    result = eden_bears
    return result

print(solution())