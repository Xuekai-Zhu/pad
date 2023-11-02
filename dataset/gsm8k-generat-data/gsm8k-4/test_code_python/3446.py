def solution():
    """A competition has racers competing on bicycles and tricycles to win a grand prize of $4000. If there are 40 people in the race, and 3/5 of them are riding on bicycles, how many wheels do the bicycles and tricycles in the race have combined?"""
    # Define the total number of racers
    total_racers = 40

    # Calculate the number of racers on bicycles
    bicycle_racers = int(total_racers * 0.6)

    # Calculate the number of racers on tricycles
    tricycle_racers = total_racers - bicycle_racers

    # Calculate the total number of wheels
    total_wheels = (bicycle_racers * 2) + (tricycle_racers * 3)

    # return the result
    result = total_wheels
    return result

print(solution())