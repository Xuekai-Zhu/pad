def solution():
    """What is the average age of the 1st and 5th fastest dogs if the 1st fastest dog is 10 years old, the 2nd fastest dog is 2 years younger than the first fastest dog, the 3rd fastest dog is 4 years older than the 2nd fastest dog, the 4th fastest dog is half the age of the 3rd fastest dog, and the 5th fastest dog is 20 years older than the 4th fastest dog?"""
    first_fastest_age = 10
    second_fastest_age = first_fastest_age - 2
    third_fastest_age = second_fastest_age + 4
    fourth_fastest_age = third_fastest_age / 2
    fifth_fastest_age = fourth_fastest_age + 20
    average_age = (first_fastest_age + fifth_fastest_age) / 2
    result = average_age
    return result

print(solution())