def solution():
    """Dilan, Martha, Phillip, and Veronica went to the park together to have some fun. They all had a different number of marbles: Dilan had 14 marbles, Martha had 20 marbles, Phillip had 19 marbles and finally, Veronica had only 7 marbles. They wanted to redistribute the marbles so they each had an equal number. How many marbles did each friend have at the end of the day?"""
    
    # Define the initial number of marbles for each friend
    dilan = 14
    martha = 20
    phillip = 19
    veronica = 7
    
    # Calculate the total number of marbles and the equal number of marbles each friend should have
    total_marbles = dilan + martha + phillip + veronica
    equal_marbles = total_marbles // 4
    
    # Redistribute the marbles equally among the friends
    dilan_final = equal_marbles - dilan
    martha_final = equal_marbles - martha
    phillip_final = equal_marbles - phillip
    veronica_final = equal_marbles - veronica
    
    # Display the final number of marbles each friend has
    result = equal_marbles
    return result

print(solution())