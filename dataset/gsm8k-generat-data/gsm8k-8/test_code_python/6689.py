def solution():
    # Define the number of shelters and people served
    num_shelters = 6
    num_people_per_shelter = 30

    # Calculate the total number of people served
    total_people_served = num_shelters * num_people_per_shelter

    # Calculate the total number of cans donated
    cans_donated = total_people_served * 10
    result = cans_donated
    return result

print(solution())