def solution():
    num_knives = 24
    num_teaspoons = 2*num_knives
    additional_knives = num_knives/3
    additional_teaspoons = 2*num_teaspoons/3

    # Calculate the total number of cutlery pieces after adding additional knives and teaspoons
    total_cutlery = num_knives + num_teaspoons + additional_knives + additional_teaspoons

    result = total_cutlery
    return result

print(solution())