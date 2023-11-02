def solution():
    """Every day, Sara bakes 10 cakes and puts them in his refrigerator. He does this for 5 days. Carol then comes over and eats 12 of his cakes. If it takes 2 cans of frosting to frost a single cake, how many cans of frosting does Bob need to frost the remaining cakes?"""
    # Define the number of cakes baked each day
    cakes_per_day = 10

    # Calculate the total number of cakes baked over 5 days
    total_cakes = cakes_per_day * 5

    # Substract the number of cakes eaten by Carol
    remaining_cakes = total_cakes - 12

    # Calculate the number of cans of frosting required to frost the remaining cakes
    frosting_cans = remaining_cakes * 2

    # Display the number of frosting cans required
    result = frosting_cans
    return result

print(solution())