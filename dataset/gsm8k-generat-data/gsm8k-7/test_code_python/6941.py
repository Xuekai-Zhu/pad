def solution():
    total_people = 200
    num_children = 80
    num_male_adults = 60

    # Calculate the number of female adults present
    num_female_adults = total_people - (num_children + num_male_adults)
    result = num_female_adults
    return result

print(solution())