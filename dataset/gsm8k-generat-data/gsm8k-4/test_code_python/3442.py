def solution():
    """Gary has 6 pounds of flour. He will use 4 pounds of flour to make cakes which require 0.5 pounds of flour each. The remaining 2 pounds of flour will be used to bake cupcakes, which require 1/5 pounds of flour. He plans to sell the cakes for $2.5 each and the cupcakes for $1 each in the school's bake sale. How much will Gary earn?"""
    # Define the amount of flour and the prices for cakes and cupcakes
    flour = 6
    cake_price = 2.5
    cupcake_price = 1

    # Calculate the number of cakes Gary can make
    cakes = 4 / 0.5

    # Calculate the number of cupcakes Gary can make
    cupcakes = 2 / (1/5)

    # Calculate the total earnings from selling cakes and cupcakes
    total_earnings = (cakes * cake_price) + (cupcakes * cupcake_price)

    result = total_earnings
    return result

print(solution())