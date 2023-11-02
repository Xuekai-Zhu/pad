def solution():
    """Steven, Stephanie, and Sonya went ice skating. Steven only fell down 3 times, but Stephanie had 13 more falls than Steven. If Sonya fell down 2 times less than half the number of times Stephanie fell, how many times did Sonya fall?"""
    # Define Steven's number of falls
    steven_falls = 3

    # Calculate Stephanie's number of falls
    stephanie_falls = steven_falls + 13

    # Calculate half the number of Stephanie's falls
    half_stephanie_falls = stephanie_falls / 2

    # Calculate Sonya's number of falls
    sonya_falls = half_stephanie_falls - 2

    # Display Sonya's number of falls
    result = sonya_falls
    return result

print(solution())