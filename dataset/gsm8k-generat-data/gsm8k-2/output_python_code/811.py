def solution():
    """Tabitha and her friends were excited to go to the Christmas parade because they knew candy would be thrown to the crowd from the floats. Tabitha caught 22 pieces of candy. Stan caught 13 pieces. Julie caught half the amount of candy as Tabitha caught and Carlos caught twice as much candy as Stan. How many pieces in total did the friends catch?"""
    tabitha_candy = 22
    stan_candy = 13
    julie_candy = tabitha_candy / 2
    carlos_candy = stan_candy * 2
    total_candy = tabitha_candy + stan_candy + julie_candy + carlos_candy
    result = total_candy
    return result

print(solution())