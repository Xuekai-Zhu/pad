def solution():
    """Dilan, Martha, Phillip, and Veronica went to the park together to have some fun. They all had a different number of marbles: Dilan had 14 marbles, Martha had 20 marbles, Phillip had 19 marbles and finally, Veronica had only 7 marbles. They wanted to redistribute the marbles so they each had an equal number. How many marbles did each friend have at the end of the day?"""
    dilan_marbles = 14
    martha_marbles = 20
    phillip_marbles = 19
    veronica_marbles = 7
    total_marbles = dilan_marbles + martha_marbles + phillip_marbles + veronica_marbles
    equal_marbles = total_marbles / 4
    result = equal_marbles
    return result

print(solution())