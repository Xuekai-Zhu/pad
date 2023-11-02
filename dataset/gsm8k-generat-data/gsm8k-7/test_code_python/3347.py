def solution():
    barbara_stuffed_animals = 9
    trish_stuffed_animals = 2 * barbara_stuffed_animals

    barbara_price = 2
    trish_price = 1.5

    # Calculate the total amount of money Barbara will donate
    barbara_donation = barbara_stuffed_animals * barbara_price

    # Calculate the total amount of money Trish will donate
    trish_donation = trish_stuffed_animals * trish_price

    # Calculate the total amount of money they will donate together
    total_donation = barbara_donation + trish_donation
    result = total_donation
    return result

print(solution())