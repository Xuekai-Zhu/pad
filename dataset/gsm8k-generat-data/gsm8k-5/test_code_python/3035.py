def solution():
    application_fee = 25  # There is a $25 application fee for each college
    num_colleges = 6  # Linda is applying to 6 colleges
    total_fee = application_fee * num_colleges  # Linda needs to pay a total of $25 * 6 = $150 in application fees
    hourly_rate = 10  # Linda makes $10 per hour babysitting

    # Calculate the number of hours Linda needs to babysit to cover the application fees
    hours_needed = total_fee / hourly_rate
    result = hours_needed
    return result

print(solution())