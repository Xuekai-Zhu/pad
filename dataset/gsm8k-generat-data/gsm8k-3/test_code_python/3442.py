def solution():
    """Gary has 6 pounds of flour. He will use 4 pounds of flour to make cakes which require 0.5 pounds of flour each.
    The remaining 2 pounds of flour will be used to bake cupcakes, which require 1/5 pounds of flour.
    He plans to sell the cakes for $2.5 each and the cupcakes for $1 each in the school's bake sale.
    How much will Gary earn?"""
    
    # Calculate the number of cakes he can make with 4 pounds of flour
    num_cakes = 4 / 0.5

    # Calculate the number of cupcakes he can make with 2 pounds of flour
    num_cupcakes = 2 / (1/5)

    # Calculate the total amount he will earn from the cakes
    cake_earnings = num_cakes * 2.5

    # Calculate the total amount he will earn from the cupcakes
    cupcake_earnings = num_cupcakes * 1

    # Calculate the total earnings
    total_earnings = cake_earnings + cupcake_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())