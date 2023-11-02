def solution():
    # Define the characteristics of oranges
    rich_vitamin_c = True
    acidic_fruit = True
    too_much_causes_issues = True
    # Check if vitamin C rich fruits can be bad for health
    if acidic_fruit and too_much_causes_issues:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())