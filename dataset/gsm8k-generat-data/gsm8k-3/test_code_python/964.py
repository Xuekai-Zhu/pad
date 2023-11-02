def solution():
    """Kevin holds the world record for eating the biggest quantity of hot wings in 8 minutes. He can eat 64 wings without stopping. Alan, a boy who loves hot wings, wants to beat Kevin's record.  He is currently able to eat 5 hot wings per minute. How many more wings must he eat per minute to beat Kevin's record?"""
    # Define Kevin's record
    kevin_record = 64

    # Define Alan's current rate of eating
    alan_rate = 5

    # Calculate Alan's current total number of wings eaten in 8 minutes
    alan_total = alan_rate * 8

    # Calculate the number of additional wings Alan needs to eat in 8 minutes to beat Kevin's record
    additional_wings = kevin_record - alan_total

    # Calculate the additional rate Alan needs to eat to beat Kevin's record
    additional_rate = additional_wings / 8

    # Display the additional rate Alan needs to eat
    result = additional_rate
    return result

print(solution())