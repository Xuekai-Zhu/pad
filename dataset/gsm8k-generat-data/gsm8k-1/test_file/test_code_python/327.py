def solution():
    '''Nick is choosing between two jobs. Job A pays $15 an hour for 2000 hours a year, and is in a state with a 20% total tax rate. Job B pays $42,000 a year and is in a state that charges $6,000 in property tax and a 10% tax rate on net income after property tax. How much more money will Nick make at the job with a higher net pay rate, compared to the other job?'''
    # Job A calculations
    jobA_hours = 2000
    jobA_pay = 15
    jobA_gross = jobA_hours * jobA_pay
    jobA_tax_rate = 0.2
    jobA_tax = jobA_gross * jobA_tax_rate
    jobA_net = jobA_gross - jobA_tax

    # Job B calculations
    jobB_salary = 42000
    jobB_property_tax = 6000
    jobB_net_income = jobB_salary - jobB_property_tax
    jobB_tax_rate = 0.1
    jobB_tax = jobB_net_income * jobB_tax_rate
    jobB_net = jobB_net_income - jobB_tax

    # Difference between net pay
    difference = jobB_net - jobA_net
    result = difference

    return result

print(solution())