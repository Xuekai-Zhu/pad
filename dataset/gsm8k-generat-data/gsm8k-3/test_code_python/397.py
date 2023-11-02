def solution():
    """Utopia National Park hosted 30,000 elephants on Friday night. The next morning, there was a 4-hour exodus out of the park, at a constant rate of 2,880 elephants/hour. Over the next 7-hour period, new elephants entered the park at a constant rate. If the final number of elephants in the park was 28,980, at what rate did the new elephants enter the park?"""
    # Define initial number of elephants
    initial_elephants = 30000

    # Define rate of exodus
    exodus_rate = 2880

    # Calculate number of elephants remaining after exodus
    remaining_elephants = initial_elephants - exodus_rate * 4

    # Define final number of elephants
    final_elephants = 28980

    # Calculate rate of entry of new elephants
    entry_rate = (final_elephants - remaining_elephants) / 7

    # Display rate of entry of new elephants
    result = entry_rate
    return result

print(solution())