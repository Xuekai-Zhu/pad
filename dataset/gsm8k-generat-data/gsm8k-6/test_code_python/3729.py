def solution():
    # Calculate the total length of the songs on Stan's playlist
    total_length = 10*3 + 15*2  # 10 3-minute songs and 15 2-minute songs

    # Calculate the additional minutes of songs needed to cover the entire run
    additional_minutes = 100 - total_length

    result = additional_minutes
    return result

print(solution())