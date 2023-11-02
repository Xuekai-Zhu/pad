def solution():
    # Calculate the number of hours Sangita has left to fly
    hours_left = 1500 - (50 + 9 + 121)

    # Calculate the number of hours Sangita must fly per month
    hours_per_month = hours_left / 6

    result = hours_per_month
    return result

print(solution())