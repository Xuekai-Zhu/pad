def solution():
    # Define the hotdog requests
    ella_request = 2
    emma_request = 2
    luke_request = 2 * (ella_request + emma_request)
    hunter_request = 1.5 * (ella_request + emma_request)

    # Calculate the total number of hotdogs needed
    total_hotdogs = ella_request + emma_request + luke_request + hunter_request
    result = total_hotdogs
    return result

print(solution())