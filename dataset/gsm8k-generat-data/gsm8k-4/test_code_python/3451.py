def solution():
    """Lyla, a grocery store owner, bought rice weighing 30 kg less than green beans, which weigh 10 kg more than sugar. While carrying the goods to the store, the bags fell down and 1/3 weight of the rice and 1/5 weight of sugar was lost. If the green beans weighed 60 kgs, then how much did the remaining stock weigh?"""
    # Define the weight of green beans
    green_beans = 60

    # Calculate the weight of sugar
    sugar = green_beans - 10

    # Calculate the weight of rice
    rice = sugar - 30

    # Calculate the weight of rice and sugar after loss
    rice_loss = rice / 3
    sugar_loss = sugar / 5
    stock_weight = rice + sugar + green_beans - rice_loss - sugar_loss

    result = stock_weight
    return result

print(solution())