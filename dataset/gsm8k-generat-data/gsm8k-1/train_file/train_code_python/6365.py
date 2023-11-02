def solution():
    """Elsa started the day with 40 marbles. At breakfast, she lost 3 marbles while playing. At lunchtime, she gave her best friend Susie 5 marbles. In the afternoon, Elsa's mom bought her a new bag with 12 marbles. Susie came back and gave Elsa twice as many marbles as she received at lunch. How many marbles did Elsa end the day with?"""
    starting_marbles = 40
    marbles_lost_at_breakfast = 3
    marbles_given_at_lunch = 5
    marbles_bought_in_afternoon = 12
    marbles_received_from_Susie = marbles_given_at_lunch * 2
    marbles_ending = starting_marbles - marbles_lost_at_breakfast + marbles_bought_in_afternoon + marbles_received_from_Susie
    result = marbles_ending
    return result

print(solution())