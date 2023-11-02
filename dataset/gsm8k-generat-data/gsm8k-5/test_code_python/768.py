def solution():
    sandoval = 12  # Governor Sandoval gave 12 commencement addresses
    hawkins = sandoval / 2  # Governor Sandoval gave twice as many as Governor Hawkins
    sloan = sandoval + 10  # Governor Sloan gave ten more than Governor Sandoval

    # Calculate total number of commencement addresses by all three governors
    total_addresses = sandoval + hawkins + sloan
    result = total_addresses
    return result

print(solution())