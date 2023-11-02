def solution():
    jack_shoes_time = 4
    toddler_shoes_time = 3
    num_toddlers = 2  # Jack has two toddlers

    # Calculate the total time it takes Jack to help both toddlers tie their shoes
    total_toddler_shoes_time = num_toddlers * toddler_shoes_time

    # Calculate the total time it takes for all of them to get ready
    total_time = jack_shoes_time + total_toddler_shoes_time
    result = total_time
    return result

print(solution())