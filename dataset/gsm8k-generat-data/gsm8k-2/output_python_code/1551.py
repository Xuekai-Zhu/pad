def solution():
    """Lauryn owns a computer company that employs men and women in different positions in the company. How many men does he employ if there are 20 fewer men than women and 180 people working for Lauryn?"""
    total_employees = 180
    women = (total_employees + 20) / 2
    men = women - 20
    result = men
    return result

print(solution())