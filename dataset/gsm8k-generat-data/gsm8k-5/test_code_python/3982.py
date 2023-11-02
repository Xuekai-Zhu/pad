def solution():
    niraj_contribution = 80  # Niraj contributed $80
    brittany_contribution = niraj_contribution * 3  # Brittany's contribution is triple Niraj's
    angela_contribution = brittany_contribution * 3  # Angela's contribution is triple Brittany's

    # Calculate the total contribution
    total_contribution = niraj_contribution + brittany_contribution + angela_contribution
    result = total_contribution
    return result

print(solution())