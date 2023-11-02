def solution():
    """Gary has 6 pounds of flour. He will use 4 pounds of flour to make cakes which require 0.5 pounds of flour each. The remaining 2 pounds of flour will be used to bake cupcakes, which require 1/5 pounds of flour. He plans to sell the cakes for $2.5 each and the cupcakes for $1 each in the school's bake sale. How much will Gary earn?"""
    total_flour = 6
    cake_flour = 4
    cake_price = 2.5
    cake_flour_per_cake = 0.5
    cupcakes_flour = total_flour - cake_flour
    cupcakes_price = 1
    cupcakes_flour_per_cupcake = 1/5
    
    num_cakes = cake_flour // cake_flour_per_cake
    cake_earnings = num_cakes * cake_price
    
    num_cupcakes = cupcakes_flour // cupcakes_flour_per_cupcake
    cupcake_earnings = num_cupcakes * cupcakes_price
    
    total_earnings = cake_earnings + cupcake_earnings
    result = total_earnings
    return result

print(solution())