def solution():
    total_people = 133
    boy_girl_difference = 33

    # Let's assume x as the number of girls
    # Then the number of boys will be x + boy_girl_difference
    # And the total number of people will be x + (x + boy_girl_difference) = 2x + boy_girl_difference = total_people
    x = (total_people - boy_girl_difference) / 2
    result = x
    return result

print(solution())