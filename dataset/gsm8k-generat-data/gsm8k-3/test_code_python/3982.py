def solution():
    """Angela's contribution is triple Brittany's contribution, and Brittany's contribution is triple Niraj's. If Niraj contributed $80, how much did everyone contribute in total?"""
    # Define Niraj's contribution
    niraj_contrib = 80

    # Calculate Brittany's and Angela's contributions
    brittany_contrib = niraj_contrib * 3
    angela_contrib = brittany_contrib * 3

    # Calculate the total contribution
    total_contrib = niraj_contrib + brittany_contrib + angela_contrib

    # Display the total contribution
    result = total_contrib
    return result

print(solution())