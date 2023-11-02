def solution():
    # Calculate the number of marbles Elsa has left after each event
    marbles_at_breakfast = 40 - 3
    marbles_at_lunch = marbles_at_breakfast - 5
    marbles_after_new_bag = marbles_at_lunch + 12
    marbles_after_exchange_with_Susie = marbles_after_new_bag + 2*(5)

    # Calculate the total number of marbles Elsa has at the end of the day
    total_marbles = marbles_after_exchange_with_Susie
    result = total_marbles
    return result

print(solution())