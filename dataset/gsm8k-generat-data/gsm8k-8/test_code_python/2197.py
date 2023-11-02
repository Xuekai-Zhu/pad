def solution():
    # Define the ratio of stubborn dog yelling to obedient dog yelling
    stubborn_to_obedient_ratio = 4/1

    # Calculate the number of times she yells at the stubborn dog
    stubborn_yelling = 12 * stubborn_to_obedient_ratio

    # Calculate the total number of times she yells at both dogs
    total_yelling = stubborn_yelling + 12

    result = total_yelling
    return result

print(solution())