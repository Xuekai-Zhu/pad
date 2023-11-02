def solution():
    """Monica way studying for an exam. She studied for 2 hours on Wednesday and three times as long on Thursday. On Friday Monica studied half of the time she studied on Thursday. During the weekend (two days) Monica studied as much again as Wednesday, Thursday and Friday combined. How much time did she spend studying in total during the five days?"""
    # Define the number of hours Monica studied on each day
    wednesday_hours = 2
    thursday_hours = 3 * wednesday_hours
    friday_hours = 0.5 * thursday_hours
    weekend_hours = (wednesday_hours + thursday_hours + friday_hours) * 2

    # Calculate the total number of hours Monica studied
    total_hours = wednesday_hours + thursday_hours + friday_hours + weekend_hours

    # Return the result
    result = total_hours
    return result

print(solution())