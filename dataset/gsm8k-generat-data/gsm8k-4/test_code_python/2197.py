def solution():
    """Missy has an obedient dog and a stubborn dog. She has to yell at the stubborn dog four times for every one time she yells at the obedient dog. If she yells at the obedient dog 12 times, how many times does she yell at both dogs combined?"""
    # Define the ratio of times Missy yells at the stubborn dog to the obedient dog
    stubborn_to_obedient_ratio = 4

    # Define the number of times Missy yells at the obedient dog
    obedient_yells = 12

    # Calculate the number of times Missy yells at the stubborn dog
    stubborn_yells = obedient_yells * stubborn_to_obedient_ratio

    # Calculate the total number of times Missy yells at both dogs
    total_yells = obedient_yells + stubborn_yells

    result = total_yells
    return result

print(solution())