def solution():
    num_people = 40
    num_cans = 600
    percent_reduction = 0.3

    # Calculate the new number of people to feed after the 30% reduction
    new_num_people = num_people - (num_people * percent_reduction)

    # Calculate the new number of cans needed to feed the new number of people
    new_num_cans = (new_num_people / num_people) * num_cans
    result = new_num_cans
    return result

print(solution())