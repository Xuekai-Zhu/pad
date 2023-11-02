def solution():
    initial_gallons = 12
    first_leg = 5 + 5
    second_leg = 6 + 2
    total_miles = first_leg + second_leg
    gallons_used = initial_gallons - 2
    mpg = total_miles / gallons_used
    result = mpg
    return result

print(solution())