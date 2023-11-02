def solution():
    
    # Define the number of cups Octavia drinks in a daily recommendation
    cups_per_recommendation = 4

    # Calculate the total number of cups Octavia drinks in a daily recommendation
    cups_per_daily_recommendation = cups_per_recommendation / 2

    # Calculate the total number of cups Juan drinks in a contract
    cups_by_contract = cups_per_daily_recommendation * 10

    # Calculate the number of cups Juan needs to reduce his daily coffee intake
    cups_to_reduce = cups_by_contract

    # Display the number of cups Juan needs to reduce
    result = cups_to_reduce
    return result

print(solution())