def solution():
    """Nancy carves statues out of jade. A giraffe statue takes 120 grams of jade and sells for $150. An elephant statue takes twice as much jade and sells for $350. If Nancy has 1920 grams of jade, how much more money will she make turning it all into elephants instead of giraffes?"""
    # Define the amount of jade and prices for each statue
    GIRAFFE_JADE = 120
    GIRAFFE_PRICE = 150
    ELEPHANT_JADE = GIRAFFE_JADE * 2
    ELEPHANT_PRICE = 350

    # Define the amount of jade Nancy has
    jade = 1920

    # Calculate the number of giraffe statues Nancy can make
    giraffe_count = jade // GIRAFFE_JADE

    # Calculate the number of elephant statues Nancy can make
    elephant_count = jade // ELEPHANT_JADE

    # Calculate the earnings for making only giraffes
    giraffe_earnings = giraffe_count * GIRAFFE_PRICE

    # Calculate the earnings for making only elephants
    elephant_earnings = elephant_count * ELEPHANT_PRICE

    # Calculate the difference in earnings between making only elephants and only giraffes
    difference = elephant_earnings - giraffe_earnings

    # Display the difference in earnings
    result = difference
    return result

print(solution())