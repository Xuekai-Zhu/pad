def solution():
    """Utopia National Park hosted 30,000 elephants on Friday night. The next morning, there was a 4-hour elephant exodus out of the park, at a constant rate of 2,880 elephants/hour. Over the next 7-hour period, new elephants entered the park at a constant rate. If the final number of elephants in the park was 28,980, at what rate did the new elephants enter the park?"""
    initial_elephants = 30000
    exodus_rate = 2880
    exodus_time = 4
    remaining_elephants = initial_elephants - (exodus_rate * exodus_time)
    final_elephants = 28980
    entering_elephants = (final_elephants - remaining_elephants) / 7
    result = entering_elephants
    return result

print(solution())