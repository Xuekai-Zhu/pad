def solution():
    poodle_time = 30  # It takes 30 minutes to groom a poodle
    terrier_time = poodle_time / 2  # It takes half as much time to groom a terrier as it takes to groom a poodle

    # Calculate the total time to groom all the poodles
    poodle_total_time = poodle_time * 3

    # Calculate the total time to groom all the terriers
    terrier_total_time = terrier_time * 8

    # Calculate the total time to groom all the dogs
    total_time = poodle_total_time + terrier_total_time
    result = total_time
    return result

print(solution())