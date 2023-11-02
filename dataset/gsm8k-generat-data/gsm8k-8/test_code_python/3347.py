def solution():
    # Define the number of stuffed animals each person has
    barbara_stuffed_animals = 9
    trish_stuffed_animals = 2 * barbara_stuffed_animals

    # Calculate the total amount of money Barbara will raise
    barbara_money = barbara_stuffed_animals * 2

    # Calculate the total amount of money Trish will raise
    trish_money = trish_stuffed_animals * 1.5

    # Calculate the total amount of money donated to the class fund
    total_money_donated = barbara_money + trish_money

    result = total_money_donated
    return result

print(solution())