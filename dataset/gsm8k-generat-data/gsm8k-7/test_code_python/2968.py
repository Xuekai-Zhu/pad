def solution():
    john_salary = 3000
    karen_salary = (4/3) * john_salary
    months_to_match = 3

    # Calculate the total amount of money John will make in the given months
    john_total = john_salary * months_to_match

    # Calculate the total amount of money Karen will make in the given months
    karen_total = karen_salary * months_to_match

    # Calculate the number of months it will take John to match Karen's total earnings
    months_to_match = karen_total / john_salary
    result = months_to_match
    return result

print(solution())