def solution():
    """Dilan, Martha, Phillip, and Veronica went to the park together to have some fun. They all had a different number of marbles: Dilan had 14 marbles, Martha had 20 marbles, Phillip had 19 marbles and finally, Veronica had only 7 marbles. They wanted to redistribute the marbles so they each had an equal number. How many marbles did each friend have at the end of the day?"""
    # Define the initial number of marbles for each friend
    dilan_marbles = 14
    martha_marbles = 20
    phillip_marbles = 19
    veronica_marbles = 7

    # Calculate the total number of marbles
    total_marbles = dilan_marbles + martha_marbles + phillip_marbles + veronica_marbles

    # Calculate the number of marbles each friend should have
    equal_marbles = total_marbles // 4

    # Calculate the number of marbles that need to be redistributed for each friend
    dilan_redistribution = equal_marbles - dilan_marbles
    martha_redistribution = equal_marbles - martha_marbles
    phillip_redistribution = equal_marbles - phillip_marbles
    veronica_redistribution = equal_marbles - veronica_marbles

    # Calculate the final number of marbles for each friend
    dilan_final = dilan_marbles + dilan_redistribution
    martha_final = martha_marbles + martha_redistribution
    phillip_final = phillip_marbles + phillip_redistribution
    veronica_final = veronica_marbles + veronica_redistribution

    # Display the final number of marbles for each friend
    result = equal_marbles
    return result

print(solution())