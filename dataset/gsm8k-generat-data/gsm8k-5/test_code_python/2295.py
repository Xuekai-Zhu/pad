def solution():
    # First find the total number of students who attended with a partner
    total_attended_with_partner = 123 - 3  # 3 students attended alone

    # Since each couple consists of 2 students, divide the total by 2 to get the number of couples
    num_couples = total_attended_with_partner / 2

    result = num_couples
    return result

print(solution())