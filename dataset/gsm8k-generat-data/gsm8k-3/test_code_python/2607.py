def solution():
    """John's dog has a litter of 8 puppies.  He gives away half of them.  He keeps one of the remaining puppies.  He then takes the remaining puppies and sells them each for $600.  He had to give the owner of the stud $300.  How much money does he profit?"""
    # Define the number of puppies and the sale price
    NUM_PUPPIES = 8
    SALE_PRICE = 600

    # Calculate the number of puppies John gives away
    given_away = NUM_PUPPIES // 2

    # Calculate the number of puppies John keeps
    kept = 1

    # Calculate the number of puppies John sells
    sold = NUM_PUPPIES - given_away - kept

    # Calculate the total revenue from selling the puppies
    revenue = sold * SALE_PRICE

    # Calculate the total expenses
    expenses = 300

    # Calculate the profit
    profit = revenue - expenses

    # Display the profit
    result = profit
    return result

print(solution())