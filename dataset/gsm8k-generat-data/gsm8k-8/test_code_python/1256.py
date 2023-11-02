def solution():
    # Calculate the total number of vegetables Conor can chop in a day
    total_veggies_per_day = 12 + 9 + 8

    # Calculate the total number of vegetables Conor can chop in a week
    total_veggies_per_week = total_veggies_per_day * 7

    # Calculate the total number of vegetables Conor can chop in 4 weeks
    total_veggies = total_veggies_per_week * 4
    result = total_veggies
    return result

print(solution())