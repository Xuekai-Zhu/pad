def solution():
    """Angela's contribution is triple Brittany's contribution, and Brittany's contribution is triple Niraj's. If Niraj contributed $80, how much did everyone contribute in total?"""
    niraj = 80
    brittany = niraj * 3
    angela = brittany * 3
    total = niraj + brittany + angela
    result = total
    return result

print(solution())