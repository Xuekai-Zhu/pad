def solution():
    total_racers = 40  # total number of racers
    bicycles = (3/5) * total_racers  # number of racers on bicycles
    tricycles = total_racers - bicycles  # number of racers on tricycles

    # Calculate the total number of wheels on the bicycles and tricycles
    total_wheels = (2 * bicycles * 2) + (3 * tricycles)  # 2 wheels on each bicycle and 3 wheels on each tricycle
    result = total_wheels
    return result

print(solution())