def solution():
    # Calculate each person's contribution
    niraj_contribution = 80 
    brittany_contribution = niraj_contribution * 3
    angela_contribution = brittany_contribution * 3

    # Calculate the total contribution
    total_contribution = niraj_contribution + brittany_contribution + angela_contribution
    result = total_contribution
    return result

print(solution())