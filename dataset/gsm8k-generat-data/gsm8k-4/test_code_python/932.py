def solution():
    """Maia is a freelance blogger working for different clients for whom she writes different articles every day. She gets 6 client requests every day and works on four of them each day. How many client requests will she have remaining to work on after 5 days?"""
    # Define the number of client requests received each day and the number worked on
    CLIENT_REQUESTS_PER_DAY = 6
    REQUESTS_WORKED_ON_PER_DAY = 4

    # Calculate the total number of requests worked on after 5 days
    requests_worked_on = REQUESTS_WORKED_ON_PER_DAY * 5

    # Calculate the total number of requests received after 5 days
    total_requests = CLIENT_REQUESTS_PER_DAY * 5

    # Calculate the number of requests remaining to work on after 5 days
    requests_remaining = total_requests - requests_worked_on

    result = requests_remaining
    return result

print(solution())