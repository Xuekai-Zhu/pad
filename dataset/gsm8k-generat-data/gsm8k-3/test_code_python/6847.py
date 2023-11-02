def solution():
    """The number of soldiers on opposite sides of a war each needs 10 pounds of food every day to continue fighting effectively. However, soldiers in the second are each given 2 pounds less food than the first side.  If the first side has 4000 soldiers and the other side 500 soldiers fewer than the first side, what's the total amount of pounds of food both sides are eating altogether every day?"""
    # Define the number of soldiers on the first side and the second side
    first_side_soldiers = 4000
    second_side_soldiers = first_side_soldiers - 500

    # Define the amount of food each soldier receives on each side
    first_side_food = 10
    second_side_food = first_side_food - 2

    # Calculate the total amount of food needed by both sides
    total_food = first_side_soldiers * first_side_food + second_side_soldiers * second_side_food

    # Display the total amount of food needed
    result = total_food
    return result

print(solution())