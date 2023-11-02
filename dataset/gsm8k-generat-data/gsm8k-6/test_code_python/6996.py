def solution():
    # Calculate Bob's weekly pay with the raise
    new_pay = (40 * (7.25 + 0.5))  # Bob works 40 hours a week and gets a raise of $0.50/hour

    # Calculate the amount of the housing benefit reduction per week
    housing_reduction = 60/4  # There are 4 weeks in a month

    # Calculate Bob's actual increase in weekly income
    actual_increase = new_pay - housing_reduction
    result = actual_increase
    return result

print(solution())