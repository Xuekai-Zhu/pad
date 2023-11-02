def solution():
    """Traci and Harris are baking cakes together. Traci has brought flour from her own house and Harris has 400g of flour in his house. Each cake needs 100g of flour and Traci and Harris have created 9 cakes each. How much flour, in grams, did Traci bring from her own house?"""
    # Define the amount of flour Harris has in his house
    harris_flour = 400

    # Define the amount of flour needed for each cake
    flour_per_cake = 100

    # Define the number of cakes Traci and Harris baked
    num_cakes = 9

    # Calculate the total amount of flour needed for all the cakes
    total_flour = flour_per_cake * num_cakes * 2

    # Calculate the amount of flour Traci brought from her own house
    traci_flour = total_flour - harris_flour

    # Display the amount of flour Traci brought
    result = traci_flour
    return result

print(solution())