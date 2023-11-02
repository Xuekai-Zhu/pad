def solution():
    """A competition has racers competing on bicycles and tricycles to win a grand prize of $4000. If there are 40 people in the race, and 3/5 of them are riding on bicycles, how many wheels do the bicycles and tricycles in the race have combined?"""
    # Define the total number of people in the race and the fraction of them riding bicycles
    total_racers = 40
    bike_fraction = 3/5

    # Calculate the number of people riding bicycles and tricycles
    bike_racers = bike_fraction * total_racers
    trike_racers = (1 - bike_fraction) * total_racers

    # Calculate the total number of wheels in the race
    bike_wheels = bike_racers * 2
    trike_wheels = trike_racers * 3
    total_wheels = bike_wheels + trike_wheels

    # Display the total number of wheels in the race
    result = total_wheels
    return result

print(solution())