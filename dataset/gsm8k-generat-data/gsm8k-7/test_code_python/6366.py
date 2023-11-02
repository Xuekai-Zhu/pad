def solution():
    starting_marbles = 40
    breakfast_loss = 3
    lunch_gift = -5
    new_bag = 12

    # Calculate the number of marbles Elsa has after breakfast
    after_breakfast = starting_marbles - breakfast_loss

    # Calculate the number of marbles Elsa has after lunch
    after_lunch = after_breakfast + lunch_gift

    # Calculate the number of marbles Elsa has after getting a new bag
    after_new_bag = after_lunch + new_bag

    # Calculate the number of marbles Elsa gets from Susie
    susie_gift = lunch_gift * 2

    # Calculate the final number of marbles Elsa has after receiving Susie's gift
    final_marbles = after_new_bag + susie_gift
    result = final_marbles
    return result

print(solution())