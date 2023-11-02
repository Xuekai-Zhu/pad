def solution():
    """Jason, Ryan, and Jeffery went fishing at the lake. Ryan caught three times the number of fish that Jason caught. Jefferey caught twice the number of fish that Ryan got. If Jeffery caught 60 fish, how many fish did all of them catch in total?"""
    # Define the number of fish caught by Jeffery
    jeffery_fish = 60

    # Calculate the number of fish caught by Ryan and Jason
    ryan_fish = jeffery_fish / 2
    jason_fish = ryan_fish / 3

    # Calculate the total number of fish caught
    total_fish = jeffery_fish + ryan_fish + jason_fish

    # return the result
    result = total_fish
    return result

print(solution())