def solution():
    """Emilia needs 42 cartons of berries to make a berry cobbler. She already has 2 cartons of strawberries and 7 cartons of blueberries in her cupboard. She decides to go to the supermarket to get more cartons. How many more cartons of berries should Emilia buy?"""
    # Define the number of cartons of strawberries and blueberries Emilia already has
    strawberries = 2
    blueberries = 7
    
    # Define the total number of cartons of berries Emilia needs
    total_needed = 42
    
    # Calculate the number of cartons of berries Emilia still needs to buy
    still_needed = total_needed - strawberries - blueberries
    
    result = still_needed
    return result

print(solution())