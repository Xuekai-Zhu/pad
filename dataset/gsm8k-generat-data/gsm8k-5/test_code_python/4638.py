def solution():
    # Cost of bread and cold cuts
    cost_bread = 3
    cost_cold_cuts = 23

    # Cost of soda and crackers
    num_people = 5
    cost_soda = 1 * num_people
    cost_crackers = 2 * 2

    # Cost of Cheese Doodles
    cost_cheese_doodles = 3 * 2 / 2

    # Cost of paper plates
    cost_paper_plates = 4

    # Total cost for each person
    total_cost_per_person = cost_bread + cost_cold_cuts + cost_soda + cost_crackers + cost_cheese_doodles + cost_paper_plates
    total_cost_rest_of_office = (total_cost_per_person * (num_people - 1))

    # Calculate the difference in cost
    difference = total_cost_per_person - total_cost_rest_of_office
    result = difference
    return result

print(solution())