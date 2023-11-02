def solution():
    """1,800 fish swim westward, 3,200 swim eastward, and 500 swim north. What is the number of fish left in the sea, if fishers catch 2/5 of the fish that swam eastward and 3/4 of the fish that swam westward?"""
    # Define the number of fish swimming in each direction
    westward_fish = 1800
    eastward_fish = 3200
    northward_fish = 500

    # Calculate the number of fish caught by fishers
    eastward_catch = 2/5 * eastward_fish
    westward_catch = 3/4 * westward_fish

    # Calculate the total number of fish left in the sea
    total_fish = westward_fish + eastward_fish + northward_fish - eastward_catch - westward_catch

    # Display the total number of fish left in the sea
    result = total_fish
    return result

print(solution())