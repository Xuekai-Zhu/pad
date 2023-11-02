def solution():
    """Nancy carves statues out of jade. A giraffe statue takes 120 grams of jade and sells for $150. An elephant statue takes twice as much jade and sells for $350. If Nancy has 1920 grams of jade, how much more money will she make turning it all into elephants instead of giraffes?"""
    # Define the weight of jade for a giraffe statue and its selling price
    giraffe_jade = 120
    giraffe_price = 150

    # Define the weight of jade for an elephant statue and its selling price
    elephant_jade = 2 * giraffe_jade
    elephant_price = 350

    # Define the total weight of jade Nancy has available
    total_jade = 1920

    # Calculate the maximum number of giraffe statues Nancy can make
    max_giraffe = total_jade // giraffe_jade

    # Calculate the maximum number of elephant statues Nancy can make
    max_elephant = total_jade // elephant_jade

    # Calculate the total earnings if Nancy makes only giraffe statues
    giraffe_earnings = max_giraffe * giraffe_price

    # Calculate the total earnings if Nancy makes only elephant statues
    elephant_earnings = max_elephant * elephant_price

    # Calculate the difference in earnings between the two options
    earnings_difference = elephant_earnings - giraffe_earnings

    # return the result
    result = earnings_difference
    return result

print(solution())