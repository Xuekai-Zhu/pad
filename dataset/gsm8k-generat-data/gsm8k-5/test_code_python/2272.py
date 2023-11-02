def solution():
    # Let x be the number of employees hired on the second week
    x = x
    # The number of employees hired on the first week is x + 200
    # The number of employees hired on the third week is x + 150
    # The number of employees hired on the fourth week is 2*(x + 150) = 2x + 300
    # The total number of employees hired in the month is x + (x + 200) + (x + 150) + (2x + 300) = 5x + 650
    # The average number of employees hired per week is (5x + 650)/4

    # Given that the number of employees hired on the fourth week was 400, we can solve for x
    # 2x + 300 = 400
    # 2x = 100
    # x = 50

    # Substituting x=50 into (5x + 650)/4 gives the average number of employees hired per week
    avg_employees_per_week = (5*50 + 650)/4
    result = avg_employees_per_week
    return result

print(solution())