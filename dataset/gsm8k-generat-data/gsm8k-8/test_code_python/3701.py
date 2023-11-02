def solution():
    # Convert the duration of the sneezing fit to seconds
    sneezing_duration = 2 * 60

    # Calculate the number of sneezes
    sneeze_frequency = 1 / 3
    number_of_sneezes = sneezing_duration * sneeze_frequency

    result = number_of_sneezes
    return result

print(solution())