def solution():
    """Utopia National Park hosted 30,000 elephants on Friday night. The next morning, there was a 4-hour elephant exodus out of the park, at a constant rate of 2,880 elephants/hour. Over the next 7-hour period, new elephants entered the park at a constant rate. If the final number of elephants in the park was 28,980, at what rate did the new elephants enter the park?"""
    # Define the initial number of elephants and the exodus rate
    initial_elephants = 30000
    exodus_rate = 2880

    # Calculate the number of elephants remaining after the exodus
    remaining_elephants = initial_elephants - exodus_rate * 4

    # Calculate the rate of new elephants entering the park
    entry_rate = (28980 - remaining_elephants) / 7

    # Return the result
    result = entry_rate
    return result

print(solution())