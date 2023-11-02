def solution():
    starting_balance = 125
    increase_percent = 0.25
    decrease_percent = 0.20

    # Calculate the amount Megan increased her savings by
    increase_amount = starting_balance * increase_percent

    # Calculate Megan's new balance after the increase
    new_balance = starting_balance + increase_amount

    # Calculate the amount Megan decreased her savings by
    decrease_amount = new_balance * decrease_percent

    # Calculate Megan's final balance
    final_balance = new_balance - decrease_amount

    # Calculate the percentage of Megan's starting balance that her final balance is
    percent_of_starting_balance = (final_balance / starting_balance) * 100
    result = percent_of_starting_balance
    return result

print(solution())