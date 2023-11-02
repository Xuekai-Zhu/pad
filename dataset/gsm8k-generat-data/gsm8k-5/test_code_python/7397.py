def solution():
    remaining_funding = 1000 - 200  # Ryan needs to raise $1000 and he already has $200
    average_funding_per_person = 10  # The average person funds $10

    # Calculate the number of people Ryan needs to recruit to fund his business
    num_people_needed = remaining_funding / average_funding_per_person
    result = num_people_needed
    return result

print(solution())