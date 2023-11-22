def solution():
    
    # Define the number of adults and children and the number of packets of chocolate bars
    num_adults = 4
    num_children = 8
    num_packets = 8

    # Calculate the total number of chocolate bars
    total_bars = num_adults * 6 + num_children * 5

    # Calculate the number of chocolate bars each child will get
    bars_per_child = total_bars // num_packets

    # Display the number of chocolate bars each child will get
    result = bars_per_child
    return result

print(solution())