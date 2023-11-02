def solution():
    # Define the number of commencement addresses each governor gave
    sandoval_addresses = 12
    hawkins_addresses = sandoval_addresses / 2
    sloan_addresses = sandoval_addresses + 10

    # Calculate the total number of commencement addresses
    total_addresses = sandoval_addresses + hawkins_addresses + sloan_addresses

    result = total_addresses
    return result

print(solution())