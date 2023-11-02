def solution():
    """Lillian is making chocolate cupcakes to sell at a fundraiser. She only has 3 cups of sugar at home. She goes to the store and buys 2 bags of sugar. Each bag of sugar contains 6 cups. The batter uses 1 cup of sugar per 12 cupcakes. She needs 2 cups of sugar to make enough frosting for a dozen cupcakes. How many dozen cupcakes can she bake and ice with the sugar she has?"""
    home_sugar = 3
    store_sugar = 2 * 6
    total_sugar = home_sugar + store_sugar
    batter_sugar_per_dozen = 1
    frosting_sugar_per_dozen = 2
    sugar_per_dozen = batter_sugar_per_dozen + frosting_sugar_per_dozen
    dozen_cupcakes = total_sugar // sugar_per_dozen
    result = dozen_cupcakes
    return result

print(solution())