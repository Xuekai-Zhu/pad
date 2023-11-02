def solution():
    """A cup of dog food weighs 1/4 of a pound.  If Mike has 2 dogs that each eat 6 cups of dog food twice a day how many 20 pound bags of dog food does he need to buy a month?"""
    # Define the weight of one cup of dog food
    CUP_WEIGHT = 0.25

    # Define the number of dogs and cups of food they eat per day
    num_dogs = 2
    cups_per_day = 6 * 2

    # Calculate the weight of dog food consumed by both dogs in one day
    total_weight_per_day = num_dogs * cups_per_day * CUP_WEIGHT

    # Calculate the weight of dog food consumed in one month (30 days)
    total_weight_per_month = total_weight_per_day * 30

    # Calculate the number of 20 pound bags of dog food needed
    num_bags = total_weight_per_month / 20

    # round up to the nearest whole bag
    num_bags = math.ceil(num_bags)

    # Display the number of bags needed
    result = num_bags
    return result

print(solution())