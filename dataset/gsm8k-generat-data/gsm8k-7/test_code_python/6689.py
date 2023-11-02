def solution():
    num_shelters = 6
    num_people_per_shelter = 30
    num_cans_per_person = 10

    # Calculate the total number of people served by all shelters combined
    total_people_served = num_shelters * num_people_per_shelter

    # Calculate the total number of cans of soup needed for all people
    total_cans_needed = total_people_served * num_cans_per_person
    result = total_cans_needed
    return result

print(solution())