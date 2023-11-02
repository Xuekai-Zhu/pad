def solution():
    money_needed = 1000
    money_raised = 200
    average_contribution = 10
    number_of_people = (money_needed - money_raised) / average_contribution
    result = number_of_people
    return result

print(solution())