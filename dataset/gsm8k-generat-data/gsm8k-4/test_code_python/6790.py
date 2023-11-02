def solution():
    """Quentin, Skylar, and Colten have a total of 383 chickens. Quentin has 25 more than double the chickens that Skylar has. Skylar has 4 less than triple the number of chickens that Colten has. How many chickens does Colten have?"""
    
    # Define the total number of chickens
    total_chickens = 383
    
    # Set up equations based on the relationships between the number of chickens each person has
    # Let x be the number of chickens Colten has
    # Then, Skylar has 3x - 4 chickens
    # And, Quentin has 2(3x-4) + 25 = 6x + 17 chickens
    # The sum of these three quantities is the total number of chickens, so we have:
    # x + (3x - 4) + (6x + 17) = 383
    # Simplifying, we get 10x + 13 = 383
    # Solving for x, we get x = 37
    
    # Calculate the number of chickens Colten has
    colten_chickens = 37
    
    result = colten_chickens
    return result

print(solution())