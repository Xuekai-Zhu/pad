def solution():
    """Jake can wash his car with 1 bottle of car wash soap 4 times. If each bottle costs $4.00, and he washes his car once a week for 20 weeks, how much does he spend on car soap?"""
    carwash_soap_price = 4
    bottles_needed_per_week = 1/4
    total_weeks = 20
    total_bottles = bottles_needed_per_week * total_weeks
    total_cost = total_bottles * carwash_soap_price
    result = total_cost
    return result

print(solution())