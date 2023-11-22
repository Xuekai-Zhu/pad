def solution():
    
    # Define the initial number of cars Robert has
    robert_cars = 20

    # Calculate the number of cars Joe has
    joe_cars = robert_cars * 2

    # Calculate the number of cars Joe sells and gives away
    sold_cars = joe_cars * 0.2
    given_away_cars = sold_cars * 2

    # Calculate the number of cars Joe has left after selling and giving away some
    remaining_cars = joe_cars - sold_cars - given_away_cars

    # Display the number of cars Joe has left
    result = remaining_cars
    return result

print(solution())