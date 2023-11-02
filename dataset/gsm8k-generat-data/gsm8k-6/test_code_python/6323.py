def solution():
    # Calculate the remaining number of jellybeans in the jar after Samantha and Shelby took some out
    remaining_jellybeans = 90 - 24 - 12

    # Calculate the amount of jellybeans Shannon refilled the jar with
    refilled_jellybeans = (24 + 12) / 2

    # Calculate the total number of jellybeans in the jar now
    total_jellybeans = remaining_jellybeans + refilled_jellybeans
    result = total_jellybeans
    return result

print(solution())