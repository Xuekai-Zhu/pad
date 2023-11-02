def solution():
    """Tabitha and her friends were excited to go to the Christmas parade because they knew candy would be thrown to the crowd from the floats.  Tabitha caught 22 pieces of candy.  Stan caught 13 pieces.  Julie caught half the amount of candy as Tabitha caught and Carlos caught twice as much candy as Stan.  How many pieces in total did the friends catch?"""
    # Total number of candy caught
    total_candy = 0

    # Add Tabitha's candy to the total
    tabitha_candy = 22
    total_candy += tabitha_candy

    # Add Stan's candy to the total
    stan_candy = 13
    total_candy += stan_candy

    # Calculate Julie's candy and add it to the total
    julie_candy = tabitha_candy / 2
    total_candy += julie_candy

    # Calculate Carlos's candy and add it to the total
    carlos_candy = stan_candy * 2
    total_candy += carlos_candy

    # Display the total number of candy caught
    result = total_candy
    return result

print(solution())