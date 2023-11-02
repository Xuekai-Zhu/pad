def solution():
    num_people = 10
    last_four_people_jellybeans = 400
    total_jellybeans = 8000

    # Calculate the total number of jellybeans taken by the last four people
    total_last_four_jellybeans = last_four_people_jellybeans * 4

    # Calculate the total number of jellybeans taken by the first six people
    total_first_six_jellybeans = total_last_four_jellybeans * 2

    # Calculate the total number of jellybeans taken by all 10 people
    total_taken_jellybeans = total_last_four_jellybeans + total_first_six_jellybeans

    # Calculate the number of jellybeans remaining in the container
    remaining_jellybeans = total_jellybeans - total_taken_jellybeans
    result = remaining_jellybeans
    return result

print(solution())