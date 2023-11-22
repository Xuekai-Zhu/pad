def solution():
    
    # Define the number of employees and their pay rates
    num_employees = 100
    junior_pay = 2000
    senior_pay = junior_pay + 400

    # Calculate the total pay for Junior programmers
    junior_total = num_employees * (2/5)
    junior_total_pay = junior_total * junior_pay

    # Calculate the total pay for Senior programmers
    senior_total_pay = senior_total * (2000 - junior_pay)

    # Calculate the total pay for all programmers
    total_pay = junior_total_pay + senior_total_pay

    # Display the total pay
    result = total_pay
    return result

print(solution())