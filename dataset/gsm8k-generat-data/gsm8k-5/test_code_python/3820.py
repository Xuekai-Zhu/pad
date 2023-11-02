def solution():
    time_per_toddler = 3  # It takes Jack 3 minutes to help each toddler with their shoes
    num_toddlers = 2  # Jack has two toddlers
    shoe_putting_time = 4  # It takes Jack 4 minutes to put his own shoes on

    # Calculate the total time it takes them to get ready
    total_time = shoe_putting_time + (num_toddlers * time_per_toddler)

    result = total_time
    return result

print(solution())