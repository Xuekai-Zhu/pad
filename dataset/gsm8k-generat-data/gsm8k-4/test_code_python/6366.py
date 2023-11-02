def solution():
    """Elsa started the day with 40 marbles.  At breakfast, she lost 3 marbles while playing.  At lunchtime, she gave her best friend Susie 5 marbles.  In the afternoon, Elsa's mom bought her a new bag with 12 marbles.  Susie came back and gave Elsa twice as many marbles as she received at lunch.  How many marbles did Elsa end the day with?"""
    # Define the initial number of marbles
    initial_marbles = 40

    # Calculate the number of marbles after breakfast
    breakfast_marbles = initial_marbles - 3

    # Calculate the number of marbles after lunch
    lunch_marbles = breakfast_marbles - 5

    # Calculate the number of marbles after getting a new bag from mom
    mom_marbles = lunch_marbles + 12

    # Calculate the number of marbles Elsa received from Susie
    susie_marbles = 2 * 5

    # Calculate the final number of marbles
    final_marbles = mom_marbles + susie_marbles

    result = final_marbles
    return result

print(solution())