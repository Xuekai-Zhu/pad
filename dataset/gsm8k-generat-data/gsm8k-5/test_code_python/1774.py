def solution():
    apple_pies = 13  # Sedrach has 13 apple pies
    samples_per_pie = 2 * 5  # Each apple pie can be divided into halves and then into 5 bite-size samples
    total_samples = apple_pies * samples_per_pie  # Calculate the total number of bite-size samples

    # Calculate the number of people who can taste the apple pies
    # Assuming each person takes one bite-size sample
    num_people = total_samples
    result = num_people
    return result

print(solution())