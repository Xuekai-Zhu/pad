def solution():
    """Silvio was running a race that had 4 parts. The total length of the race was 74.5 kilometers. The first part of the race is 15.5 kilometers long. The second and third parts are each 21.5 kilometers long. How many kilometers is the last part of the race?"""
    # Define the lengths of each part of the race
    part1 = 15.5
    part2 = 21.5
    part3 = 21.5

    # Calculate the length of the last part of the race
    part4 = 74.5 - part1 - part2 - part3

    # Display the length of the last part of the race
    result = part4
    return result

print(solution())