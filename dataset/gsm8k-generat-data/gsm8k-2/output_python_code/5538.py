def solution():
    """Monica way studying for an exam. She studied for 2 hours on Wednesday and three times as long on Thursday. On Friday Monica studied half of the time she studied on Thursday. During the weekend (two days) Monica studied as much again as Wednesday, Thursday and Friday combined. How much time did she spend studying in total during the five days?"""
    wednesday_time = 2
    thursday_time = 3 * wednesday_time
    friday_time = 0.5 * thursday_time
    weekend_time = (wednesday_time + thursday_time + friday_time) * 2
    total_time = wednesday_time + thursday_time + friday_time + weekend_time
    result = total_time
    return result

print(solution())