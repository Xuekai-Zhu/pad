def solution():
    """Aaron and his brother Carson each saved up $40 to go to dinner. The bill is 3/4 of their total money. After, they go out for ice cream. Each scoop costs $1.5 and they get the same amount as each other. If they leave with $1 in change each, how many scoops did they each buy?"""
    # Calculate the total amount of money they have for dinner and ice cream
    total_money = 2 * 40 - 2  # They both saved $40 and spent $1 in change each
    dinner_bill = 3 * total_money / 4  # The bill for dinner is 3/4 of their total money
    ice_cream_money = total_money - dinner_bill  # The rest of the money is for ice cream

    # Calculate how many scoops they each bought
    num_scoops_each = (ice_cream_money - 2) / 3  # They each left with $1 in change

    # Display the number of scoops they each bought
    result = num_scoops_each
    return result

print(solution())