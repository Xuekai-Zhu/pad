def solution():
    """Ken caught twice as many fish as Kendra, but Ken released 3 fish back into the lake. Kendra caught 30 fish and did not release any of them back into the lake. How many fish did Ken and Kendra bring home?"""
    # Define Kendra's number of caught fish
    kendra_fish = 30

    # Calculate Ken's number of caught fish
    ken_fish = kendra_fish * 2 - 3

    # Calculate the total number of fish caught
    total_fish = kendra_fish + ken_fish

    # Display the number of fish caught by Ken and Kendra
    result = (ken_fish, kendra_fish)
    return result

print(solution())