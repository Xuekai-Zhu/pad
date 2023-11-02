def solution():
    # Calculate the initial number of girls in the classroom
    initial_num_girls = int(20 * 0.4)

    # Calculate the initial percentage of girls in the classroom
    initial_percentage_girls = (initial_num_girls / 20) * 100

    # Calculate the new number of boys in the classroom after 5 new boys join
    new_num_boys = 20 - initial_num_girls + 5

    # Calculate the new number of girls in the classroom after 5 new boys join
    new_num_girls = 20 - new_num_boys

    # Calculate the new percentage of girls in the classroom
    new_percentage_girls = (new_num_girls / 20) * 100

    result = new_percentage_girls
    return result

print(solution())