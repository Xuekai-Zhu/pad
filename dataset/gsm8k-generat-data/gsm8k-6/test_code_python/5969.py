def solution():
    # Calculate the number of racers remaining after each segment
    remaining_racers = 100 - 10  # 10 racers eliminated after the first segment
    remaining_racers = remaining_racers - (remaining_racers // 3)  # A third of the remaining racers are eliminated after the next section
    remaining_racers = remaining_racers // 2  # Half of the remaining racers are eliminated before the last leg of the race

    result = remaining_racers
    return result

print(solution())