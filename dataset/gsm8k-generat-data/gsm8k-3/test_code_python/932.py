def solution():
    """Maia is a freelance blogger working for different clients for whom she writes different articles every day. She gets 6 client requests every day and works on four of them each day. How many client requests will she have remaining to work on after 5 days."""
    # Define the number of client requests received each day and the number of requests worked on each day
    CLIENT_REQUESTS_PER_DAY = 6
    REQUESTS_WORKED_ON_PER_DAY = 4

    # Calculate the total number of client requests received and worked on over 5 days
    total_requests_received = CLIENT_REQUESTS_PER_DAY * 5
    total_requests_worked_on = REQUESTS_WORKED_ON_PER_DAY * 5

    # Calculate the number of client requests remaining to work on after 5 days
    requests_remaining = total_requests_received - total_requests_worked_on

    # Display the number of requests remaining
    result = requests_remaining
    return result

print(solution())