def solution():
    """Sean played cricket for 50 minutes each day for 14 days. Indira also played cricket. Together they played cricket for 1512 minutes. How many minutes did Indira play cricket?"""
    # Define the number of minutes Sean played cricket
    sean_minutes = 50 * 14

    # Calculate the number of minutes Indira played cricket
    indira_minutes = 1512 - sean_minutes

    # Return the result
    result = indira_minutes
    return result

print(solution())