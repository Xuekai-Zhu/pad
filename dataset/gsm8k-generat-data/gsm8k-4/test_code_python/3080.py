def solution():
    """Tony has two fish. Every year, his parents buy him two more, but one of them dies. How many fish will he have in five years?"""
    
    # Initialize the number of fish
    num_fish = 2

    # Loop through five years, adding and subtracting fish each year
    for i in range(5):
        num_fish += 1 # Tony starts with 2 fish and gets 2 more each year
        num_fish -= 1 # One of the fish dies each year
        
    # Return the final number of fish
    result = num_fish
    return result

print(solution())