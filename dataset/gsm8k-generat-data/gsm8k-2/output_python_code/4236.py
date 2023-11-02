def solution():
    """Silvio was running a race that had 4 parts. The total length of the race was 74.5 kilometers. The first part of the race is 15.5 kilometers long. The second and third parts are each 21.5 kilometers long. How many kilometers is the last part of the race?"""
    total_length = 74.5
    first_part = 15.5
    second_part = 21.5
    third_part = 21.5
    last_part = total_length - first_part - second_part - third_part
    result = last_part
    return result

print(solution())