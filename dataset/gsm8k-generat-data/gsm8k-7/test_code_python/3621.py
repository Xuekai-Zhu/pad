def solution():
    fiona_hours = 40
    john_hours = 30
    jeremy_hours = 25
    hourly_rate = 20

    # Calculate Fiona's monthly pay
    fiona_pay = fiona_hours * hourly_rate * 4

    # Calculate John's monthly pay
    john_pay = john_hours * hourly_rate * 4

    # Calculate Jeremy's monthly pay
    jeremy_pay = jeremy_hours * hourly_rate * 4

    # Calculate the total monthly pay for all employees
    total_pay = fiona_pay + john_pay + jeremy_pay
    result = total_pay
    return result

print(solution())