def solution():
    """Lillian is making chocolate cupcakes to sell at a fundraiser. She only has 3 cups of sugar at home. She goes to the store and buys 2 bags of sugar. Each bag of sugar contains 6 cups. The batter uses 1 cup of sugar per 12 cupcakes. She needs 2 cups of sugar to make enough frosting for a dozen cupcakes. How many dozen cupcakes can she bake and ice with the sugar she has?"""
    # Define the total amount of sugar Lillian has
    total_sugar = 3 + 2 * 6

    # Calculate the number of cupcakes Lillian can make with the sugar
    cupcakes = total_sugar / 1

    # Calculate the number of dozens of cupcakes Lillian can make
    dozens = cupcakes / 12

    # Calculate the amount of sugar needed for the frosting
    frosting_sugar = dozens * 2

    # Check if Lillian has enough sugar for the frosting
    if frosting_sugar <= total_sugar:
        result = int(dozens)
    else:
        result = 0
    return result

print(solution())