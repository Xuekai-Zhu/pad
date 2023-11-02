def solution():
    """Carla, Kyle, and Tasha caught 36 fish. If Kyle and Tasha caught the same number of fish and Carla caught 8, how many fish did Kyle catch?"""
    # Define the number of fish Carla caught
    carla_fish = 8

    # Calculate the total number of fish caught by Kyle and Tasha
    kyle_tasha_fish = 36 - carla_fish

    # Divide the total number of fish caught by Kyle and Tasha by 2 to get the number of fish caught by each
    kyle_fish = kyle_tasha_fish / 2

    # Display the number of fish caught by Kyle
    result = kyle_fish
    return result

print(solution())