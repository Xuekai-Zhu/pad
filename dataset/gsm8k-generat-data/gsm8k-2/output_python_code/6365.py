def solution():
    """Elsa started the day with 40 marbles. At breakfast, she lost 3 marbles while playing. At lunchtime, she gave her best friend Susie 5 marbles. In the afternoon, Elsa's mom bought her a new bag with 12 marbles. Susie came back and gave Elsa twice as many marbles as she received at lunch. How many marbles did Elsa end the day with?"""
    starting_marbles = 40
    breakfast_loss = 3
    lunch_gift = 5
    afternoon_gain = 12
    susie_gift = lunch_gift * 2

    remaining_marbles = starting_marbles - breakfast_loss - lunch_gift + afternoon_gain + susie_gift
    result = remaining_marbles
    return result

print(solution())