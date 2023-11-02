def solution():
    spaying_cost = 200
    num_vaccines = 3
    vaccine_cost = 20
    num_vases_broken = 4
    vases_cost = 12

    # Calculate the total cost of all vaccines
    total_vaccine_cost = num_vaccines * vaccine_cost

    # Calculate the total cost of all vases
    total_vases_cost = num_vases_broken * vases_cost

    # Calculate the total cost of the kitten
    total_kitten_cost = spaying_cost + total_vaccine_cost + total_vases_cost
    result = total_kitten_cost
    return result

print(solution())