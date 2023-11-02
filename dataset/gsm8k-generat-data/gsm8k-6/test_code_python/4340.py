def solution():
    # Calculate the total amount Claudia makes from Saturday's class
    saturday_kids = 20
    saturday_income = saturday_kids * 10

    # Calculate the total amount Claudia makes from Sunday's class
    sunday_kids = 10  # half of 20
    sunday_income = sunday_kids * 10

    # Calculate the total income
    total_income = saturday_income + sunday_income
    result = total_income
    return result

print(solution())