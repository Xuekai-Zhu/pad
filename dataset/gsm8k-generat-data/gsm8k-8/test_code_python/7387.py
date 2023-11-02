def solution():
    # Calculate Amanda's total pay for the day
    total_pay = 50 * 10

    # Calculate the amount of pay she will lose if she does not finish the report
    withheld_pay = 0.2 * total_pay

    # Calculate Amanda's final pay if she does not finish the report
    final_pay = total_pay - withheld_pay
    result = final_pay
    return result

print(solution())