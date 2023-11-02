def solution():
    # Calculate the number of female members in the club
    total_members = 18
    male_members = total_members / 3  # since there are three times as many male members as female members
    female_members = male_members * 2  # since there are two times as many female members as male members
    result = female_members
    return result

print(solution())