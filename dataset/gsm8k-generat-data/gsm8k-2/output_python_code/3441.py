def solution():
    """Gary has 6 pounds of flour. He will use 4 pounds of flour to make cakes which require 0.5 pounds of flour each. The remaining 2 pounds of flour will be used to bake cupcakes, which require 1/5 pounds of flour. He plans to sell the cakes for $2.5 each and the cupcakes for $1 each in the school's bake sale. How much will Gary earn?"""
    total_flour = 6
    cake_flour = 4
    cake_count = cake_flour / 0.5
    cupcake_flour = total_flour - cake_flour
    cupcake_count = cupcake_flour / (1/5)
    cake_income = cake_count * 2.5
    cupcake_income = cupcake_count * 1
    total_income = cake_income + cupcake_income
    result = total_income
    return result

print(solution())