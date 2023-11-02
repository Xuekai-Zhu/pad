def solution():
    """When Jack traveled to Canada, he had to wait 20 hours to get through customs, plus 14 days in coronavirus quarantine. How many hours total did Jack have to wait?"""
    # Define the number of hours in a day
    HOURS_PER_DAY = 24

    # Define the number of hours Jack had to wait in customs and quarantine
    customs_wait = 20
    quarantine_wait = 14 * HOURS_PER_DAY

    # Calculate the total number of hours Jack had to wait
    total_wait = customs_wait + quarantine_wait

    # return the result
    result = total_wait
    return result

print(solution())