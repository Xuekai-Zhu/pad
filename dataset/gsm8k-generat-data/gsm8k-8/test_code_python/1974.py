def solution():
    # Calculate middle school allowance
    middle_school = 8 + 2

    # Calculate senior year allowance
    senior_year = 5 + 2 * middle_school

    # Calculate percentage increase
    percentage_increase = (senior_year - middle_school) / middle_school * 100

    result = percentage_increase
    return result

print(solution())