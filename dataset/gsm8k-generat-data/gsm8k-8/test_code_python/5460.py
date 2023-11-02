def solution():
    # Define the total amount of coffee that Omar buys
    total_coffee = 12

    # Calculate how much coffee Omar drinks on his way to work
    coffee_on_way_to_work = total_coffee * 0.25

    # Calculate how much coffee Omar drinks at his office
    coffee_at_office = (total_coffee - coffee_on_way_to_work) * 0.5

    # Calculate how much coffee Omar has left to drink
    coffee_left = total_coffee - coffee_on_way_to_work - coffee_at_office

    # Calculate how much coffee Omar drinks when he remembers it is cold
    coffee_drunk_when_cold = 1

    # Calculate how much coffee Omar has left in the cup
    coffee_left_in_cup = coffee_left - coffee_drunk_when_cold

    result = coffee_left_in_cup
    return result

print(solution())