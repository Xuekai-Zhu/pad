def solution():
    sandoval_addresses = 12
    hawkins_addresses = sandoval_addresses / 2
    sloan_addresses = sandoval_addresses + 10

    # Calculate the total number of addresses given by all three governors
    total_addresses = sandoval_addresses + hawkins_addresses + sloan_addresses
    result = total_addresses
    return result

print(solution())