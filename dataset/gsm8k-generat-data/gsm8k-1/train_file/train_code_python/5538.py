def solution():
    """Monica way studying for an exam. She studied for 2 hours on Wednesday and three times as long on Thursday. On Friday Monica studied half of the time she studied on Thursday. During the weekend (two days) Monica studied as much again as Wednesday, Thursday and Friday combined. How much time did she spend studying in total during the five days?"""
    wednesday_hours = 2
    thursday_hours = wednesday_hours * 3
    friday_hours = thursday_hours / 2
    weekend_hours = (wednesday_hours + thursday_hours + friday_hours) * 2
    total_hours = wednesday_hours + thursday_hours + friday_hours + weekend_hours
    result = total_hours
    return result

print(solution())