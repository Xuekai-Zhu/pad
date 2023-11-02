def solution():
    # Calculate the number of smoking students
    num_smokers = 0.4 * 300

    # Calculate the number of smoking students hospitalized
    num_hospitalized = 0.7 * num_smokers

    # Calculate the number of smoking students not hospitalized
    num_not_hospitalized = num_smokers - num_hospitalized
    result = num_not_hospitalized
    return result

print(solution())