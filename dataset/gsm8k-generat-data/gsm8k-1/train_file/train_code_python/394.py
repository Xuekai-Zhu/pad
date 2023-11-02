def solution():
    """Utopia National Park hosted 30,000 elephants on Friday night. The next morning, there was a 4-hour elephant exodus out of the park, at a constant rate of 2,880 elephants/hour. Over the next 7-hour period, new elephants entered the park at a constant rate. If the final number of elephants in the park was 28,980, at what rate did the new elephants enter the park?"""
    initial_elephants = 30000
    exiting_rate = 2880
    exiting_time = 4
    exiting_amount = exiting_rate * exiting_time
    remaining_elephants = initial_elephants - exiting_amount
    final_elephants = 28980
    entering_time = 7
    entering_amount = final_elephants - remaining_elephants
    entering_rate = entering_amount / entering_time
    result = entering_rate
    return result

print(solution())