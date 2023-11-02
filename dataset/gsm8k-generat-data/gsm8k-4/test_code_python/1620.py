def solution():
    """When Michelle makes fresh pasta, she first makes the dough, then she rolls it out and cuts it, and then she hangs it on racks to dry for cooking later. She needs a drying rack for each three pounds of pasta she makes, and it takes two cups of flour to make each pound of pasta dough. She owns three racks right now. How many more drying racks will Michelle need if she makes pasta using three 8-cup bags of flour?"""
    # Define the number of racks owned by Michelle
    owned_racks = 3

    # Define the amount of flour needed to make one pound of pasta
    flour_per_pound = 2

    # Define the amount of pasta that can be made with three 8-cup bags of flour
    total_pasta = (3 * 8) / flour_per_pound

    # Define the number of racks needed for the total amount of pasta
    needed_racks = total_pasta / 3

    # Calculate the additional number of racks needed
    additional_racks = needed_racks - owned_racks

    result = additional_racks
    return result

print(solution())