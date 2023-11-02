def solution():
    """Andrew has 2 3-hour appointments today. He spends the rest of his 8-hour workday stamping permit applications. If he can stamp 50 permit applications an hour, how many permits total does he stamp today?"""
    # Calculate the total time Andrew has for stamping permits
    total_time = 8 - 3*2

    # Calculate the total number of permits Andrew can stamp
    total_permits = total_time * 50

    # Display the total number of permits
    result = total_permits
    return result

print(solution())