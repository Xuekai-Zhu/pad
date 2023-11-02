def solution():
    """Lillian is making chocolate cupcakes to sell at a fundraiser. She only has 3 cups of sugar at home. She goes to the store and buys 2 bags of sugar. Each bag of sugar contains 6 cups. The batter uses 1 cup of sugar per 12 cupcakes. She needs 2 cups of sugar to make enough frosting for a dozen cupcakes. How many dozen cupcakes can she bake and ice with the sugar she has?"""
    initial_sugar = 3
    additional_sugar = 2 * 6
    total_sugar = initial_sugar + additional_sugar
    sugar_per_dozen_cupcakes = 1 + 2
    dozens_of_cupcakes = total_sugar // sugar_per_dozen_cupcakes
    result = dozens_of_cupcakes
    return result

print(solution())