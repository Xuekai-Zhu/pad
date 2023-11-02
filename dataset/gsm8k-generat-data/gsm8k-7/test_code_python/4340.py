def solution():
    num_kids_saturday = 20
    num_kids_sunday = num_kids_saturday / 2
    cost_per_class = 10.0

    # Calculate the total amount of money Claudia makes from Saturday's class
    saturday_income = num_kids_saturday * cost_per_class

    # Calculate the total amount of money Claudia makes from Sunday's class
    sunday_income = num_kids_sunday * cost_per_class

    # Calculate the total amount of money Claudia makes from both classes
    total_income = saturday_income + sunday_income
    result = total_income
    return result

print(solution())