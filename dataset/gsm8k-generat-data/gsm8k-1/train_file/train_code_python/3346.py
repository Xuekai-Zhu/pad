def solution():
    """Barbara has 9 stuffed animals. Trish has two times as many stuffed animals as Barbara. They planned to sell their stuffed animals and donate all the money to their class funds. Barbara will sell her stuffed animals for $2 each while Trish will sell them for $1.50 each. How much money will they donate to their class funds?"""
    barbara_animals = 9
    trish_animals = 2 * barbara_animals
    barbara_price = 2
    trish_price = 1.5
    total_donation = (barbara_animals * barbara_price) + (trish_animals * trish_price)
    result = total_donation
    return result

print(solution())