def solution():
    initial_marbles = 40  # Elsa starts with 40 marbles
    lost_at_breakfast = 3  # Elsa loses 3 marbles at breakfast
    given_at_lunch = 5  # Elsa gives 5 marbles to Susie at lunch
    received_in_afternoon = 12  # Elsa receives 12 marbles in the afternoon
    given_back_by_susie = given_at_lunch * 2  # Susie gives back twice as many marbles as she received

    # Calculate the total number of marbles Elsa ends the day with
    end_marbles = initial_marbles - lost_at_breakfast + received_in_afternoon - given_at_lunch + given_back_by_susie
    result = end_marbles
    return result

print(solution())