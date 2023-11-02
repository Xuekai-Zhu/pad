def solution():
    # Calculate the number of pots produced in the first hour
    first_hour_pots = 60 // 6  # 60 minutes in an hour, it takes 6 minutes to produce one pot

    # Calculate the number of pots produced in the last hour
    last_hour_pots = 60 // 5  # 60 minutes in an hour, it takes 5 minutes to produce one pot

    # Calculate the additional pots produced in the last hour compared to the first
    additional_pots = last_hour_pots - first_hour_pots
    result = additional_pots
    return result

print(solution())