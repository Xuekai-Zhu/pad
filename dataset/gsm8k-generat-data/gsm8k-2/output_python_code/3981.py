def solution():
    """Angela's contribution is triple Brittany's contribution, and Brittany's contribution is triple Niraj's. If Niraj contributed $80, how much did everyone contribute in total?"""
    niraj_contribution = 80
    brittany_contribution = niraj_contribution * 3
    angela_contribution = brittany_contribution * 3
    total_contribution = niraj_contribution + brittany_contribution + angela_contribution
    result = total_contribution
    return result

print(solution())