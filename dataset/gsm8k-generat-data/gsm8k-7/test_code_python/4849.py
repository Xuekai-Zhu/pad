def solution():
    poodle_time = 30
    terrier_time = poodle_time / 2

    num_poodles = 3
    num_terriers = 8

    # Calculate the total time to groom all poodles
    total_poodle_time = num_poodles * poodle_time

    # Calculate the total time to groom all terriers
    total_terrier_time = num_terriers * terrier_time

    # Calculate the total time to groom all dogs
    total_time = total_poodle_time + total_terrier_time
    result = total_time
    return result

print(solution())