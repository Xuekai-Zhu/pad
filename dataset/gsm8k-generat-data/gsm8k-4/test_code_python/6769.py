def solution():
    """Ken caught twice as many fish as Kendra, but Ken released 3 fish back into the lake. Kendra caught 30 fish and did not release any of them back into the lake. How many fish did Ken and Kendra bring home?"""
    # Define the number of fish caught by Kendra and Ken
    kendras_fish = 30
    kens_fish = kendras_fish * 2 - 3   # since Ken released 3 fish

    # Calculate the total number of fish caught and brought home
    total_fish = kendras_fish + kens_fish

    # Return the result
    result = total_fish
    return result

print(solution())