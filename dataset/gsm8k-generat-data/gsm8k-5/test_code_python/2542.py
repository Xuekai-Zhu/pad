def solution():
    # Calculate the number of pots produced in the first hour
    pots_first_hour = 60 // 6  # 60 minutes divided by 6 minutes per pot

    # Calculate the number of pots produced in the last hour
    pots_last_hour = 60 // 5  # 60 minutes divided by 5 minutes per pot

    # Calculate the additional pots produced in the last hour compared to the first
    additional_pots = pots_last_hour - pots_first_hour
    result = additional_pots
    return result

print(solution())