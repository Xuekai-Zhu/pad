def solution():
    # Define the ratio of Halima's age to Beckham's age to Michelle's age
    ratio = "4:3:7"

    # Calculate the sum of the parts of the ratio
    total_parts = sum([int(part) for part in ratio.split(":")])

    # Calculate the age of each sibling using the ratio and the total age
    halima_age = int(ratio.split(":")[0]) / total_parts * 126
    beckham_age = int(ratio.split(":")[1]) / total_parts * 126

    # Calculate the age difference between Halima and Beckham
    age_difference = abs(halima_age - beckham_age)
    result = age_difference
    return result

print(solution())