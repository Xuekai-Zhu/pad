def solution():
    salary = 40000  # Steve makes 40000$ a year as a teacher
    taxes = 0.2 * salary  # He loses 20 percent to taxes
    healthcare = 0.1 * salary  # He loses 10 percent to healthcare
    union_dues = 800  # He pays 800$ to local union dues

    # Calculate Steve's take-home pay
    take_home_pay = salary - taxes - healthcare - union_dues
    result = take_home_pay
    return result

print(solution())