def solution():
    """Elsa started the day with 40 marbles.  At breakfast, she lost 3 marbles while playing.  At lunchtime, she gave her best friend Susie 5 marbles.  In the afternoon, Elsa's mom bought her a new bag with 12 marbles.  Susie came back and gave Elsa twice as many marbles as she received at lunch.  How many marbles did Elsa end the day with?"""
    # Define the starting number of marbles
    STARTING_MARBLES = 40

    # Calculate the number of marbles Elsa has after breakfast
    breakfast_loss = 3
    marbles_after_breakfast = STARTING_MARBLES - breakfast_loss

    # Calculate the number of marbles Elsa has after lunch
    lunch_gift = 5
    marbles_after_lunch = marbles_after_breakfast - lunch_gift

    # Calculate the number of marbles Elsa has after getting the new bag
    new_bag = 12
    marbles_after_bag = marbles_after_lunch + new_bag

    # Calculate the number of marbles Elsa has at the end of the day
    susie_gift = lunch_gift * 2
    end_of_day_marbles = marbles_after_bag + susie_gift

    # Display the number of marbles Elsa has at the end of the day
    result = end_of_day_marbles
    return result

print(solution())