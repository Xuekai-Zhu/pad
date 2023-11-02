def solution():
    # Define the number of jelly beans taken by the last four people
    last_four_jelly_beans = 400

    # Calculate the total number of jelly beans taken by the last four people
    last_four_total = last_four_jelly_beans * 4

    # Calculate the total number of jelly beans taken by the first six people
    first_six_total = last_four_total * 2

    # Calculate the total number of jelly beans taken by all 10 people
    total_taken = first_six_total + last_four_total

    # Calculate the number of jelly beans remaining in the container
    remaining = 8000 - total_taken
    result = remaining
    return result

print(solution())