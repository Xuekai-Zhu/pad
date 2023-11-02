def solution():
    """ Scout delivers groceries on the weekends.  His base pay is $10.00 an hour.  He also earns a $5.00 tip per customer that he delivers groceries to.  On Saturday he worked 4 hours and delivered groceries to 5 people.  Sunday he worked 5 hours and delivered groceries to 8 people.  How much did he make over the weekend? """
    # Define Scout's base pay and tip amount
    BASE_PAY = 10
    TIP = 5

    # Calculate Scout's earnings on Saturday
    saturday_hours = 4
    saturday_customers = 5
    saturday_pay = saturday_hours * BASE_PAY + saturday_customers * TIP

    # Calculate Scout's earnings on Sunday
    sunday_hours = 5
    sunday_customers = 8
    sunday_pay = sunday_hours * BASE_PAY + sunday_customers * TIP

    # Calculate Scout's total earnings over the weekend
    total_pay = saturday_pay + sunday_pay

    # Display Scout's total earnings
    result = total_pay
    return result

print(solution())