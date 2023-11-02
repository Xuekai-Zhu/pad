def solution():
    """Daragh had 20 stuffed bears. She took out her favorite 8 bears and then equally divided the other bears among her 3 sisters. Daragh's youngest sister, Eden, already had 10 stuffed bears. How many stuffed bears does Eden have now?"""
    initial_bears = 20
    favorite_bears = 8
    remaining_bears = initial_bears - favorite_bears
    sisters = 3
    divided_bears = remaining_bears // sisters
    eden_bears = divided_bears + 10
    result = eden_bears
    return result

print(solution())