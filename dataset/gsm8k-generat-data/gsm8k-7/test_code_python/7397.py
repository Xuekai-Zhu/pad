def solution():
    average_funding_per_person = 10
    current_funding = 200
    total_project_cost = 1000

    # Calculate the amount of funding still needed
    remaining_funding_needed = total_project_cost - current_funding

    # Calculate the number of people Ryan needs to recruit to fund the project
    num_people_needed = remaining_funding_needed / average_funding_per_person
    result = num_people_needed
    return result

print(solution())