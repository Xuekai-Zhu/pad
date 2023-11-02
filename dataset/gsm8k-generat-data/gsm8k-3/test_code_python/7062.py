def solution():
    """Jason, Ryan, and Jeffery went fishing at the lake. Ryan caught three times the number of fish that Jason caught. Jefferey caught twice the number of fish that Ryan got. If Jeffery caught 60 fish, how many fish did all of them catch in total?"""
    # Calculate the number of fish caught by Ryan
    ryan_catch = 3 * jason_catch

    # Calculate the total number of fish caught
    total_catch = jason_catch + ryan_catch + jeffery_catch

    # Display the total number of fish caught
    result = total_catch
    return result

print(solution())