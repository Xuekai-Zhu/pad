def solution():
    lily_time = 5
    rose_time = 7
    orchid_time = 3
    vine_time = 2

    num_lilies = 17
    num_roses = 10
    num_orchids = 6
    num_vines = 20

    # Calculate the total time to paint all lilies
    total_lily_time = num_lilies * lily_time

    # Calculate the total time to paint all roses
    total_rose_time = num_roses * rose_time

    # Calculate the total time to paint all orchids
    total_orchid_time = num_orchids * orchid_time

    # Calculate the total time to paint all vines
    total_vine_time = num_vines * vine_time

    # Calculate the total time to paint all flowers
    total_time = total_lily_time + total_rose_time + total_orchid_time + total_vine_time
    result = total_time
    return result

print(solution())