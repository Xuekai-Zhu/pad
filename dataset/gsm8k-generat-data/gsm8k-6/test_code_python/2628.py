def solution():
    # Calculate the total amount of money John has to buy birds
    total_money = 50*4  # John got 50 dollars from each of his 4 grandparents

    # Calculate the total number of birds John can buy
    total_birds = total_money//20  # Each bird costs $20

    # Calculate the total number of wings of all birds
    total_wings = total_birds*2  # Each bird has 2 wings

    result = total_wings
    return result

print(solution())