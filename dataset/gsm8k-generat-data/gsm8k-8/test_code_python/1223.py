def solution():
    # Define the number of falls for Steven and Stephanie
    steven_falls = 3
    stephanie_falls = steven_falls + 13

    # Calculate the number of falls for Sonya
    sonya_falls = (stephanie_falls / 2) - 2
    result = sonya_falls
    return result

print(solution())