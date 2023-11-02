def solution():
    """Angela's contribution is triple Brittany's contribution, and Brittany's contribution is triple Niraj's. If Niraj contributed $80, how much did everyone contribute in total?"""
    # Define Niraj's contribution
    niraj_contribution = 80

    # Calculate Brittany's contribution
    brittany_contribution = niraj_contribution * 3

    # Calculate Angela's contribution
    angela_contribution = brittany_contribution * 3

    # Calculate the total contribution
    total_contribution = niraj_contribution + brittany_contribution + angela_contribution

    result = total_contribution
    return result

print(solution())