def solution():
    """Lillian is making chocolate cupcakes to sell at a fundraiser. She only has 3 cups of sugar at home. She goes to the store and buys 2 bags of sugar. Each bag of sugar contains 6 cups. The batter uses 1 cup of sugar per 12 cupcakes. She needs 2 cups of sugar to make enough frosting for a dozen cupcakes. How many dozen cupcakes can she bake and ice with the sugar she has?"""
    
    # Calculate the total amount of sugar Lillian has
    sugar_total = 3 + 2*6 # 2 bags of 6 cups each

    # Calculate the amount of sugar needed for a dozen cupcakes
    sugar_per_dozen = 1 + 2 # 1 cup for batter, 2 cups for frosting

    # Calculate the maximum number of dozens of cupcakes Lillian can make
    max_dozen = sugar_total // sugar_per_dozen

    # Display the maximum number of dozens of cupcakes Lillian can make
    result = max_dozen
    return result

print(solution())