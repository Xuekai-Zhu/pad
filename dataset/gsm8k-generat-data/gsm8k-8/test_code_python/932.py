def solution():
    # Calculate the total number of client requests over 5 days
    total_requests = 6 * 5

    # Calculate the number of requests Maia completes over 5 days
    completed_requests = 4 * 5

    # Calculate the remaining requests after 5 days
    remaining_requests = total_requests - completed_requests

    result = remaining_requests
    return result

print(solution())