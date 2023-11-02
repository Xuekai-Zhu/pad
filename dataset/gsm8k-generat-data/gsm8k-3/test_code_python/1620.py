def solution():
    """When Michelle makes fresh pasta, she first makes the dough, then she rolls it out and cuts it, and then she hangs it on racks to dry for cooking later. She needs a drying rack for each three pounds of pasta she makes, and it takes two cups of flour to make each pound of pasta dough. She owns three racks right now. How many more drying racks will Michelle need if she makes pasta using three 8-cup bags of flour?"""
    # Define the number of cups of flour needed to make each pound of pasta dough
    CUPS_PER_POUND = 2

    # Define the number of pounds of pasta that can be made from 3 8-cup bags of flour
    bags_of_flour = 3
    pounds_of_pasta = bags_of_flour * 4

    # Calculate the number of racks needed for the pasta
    racks_needed = pounds_of_pasta // 3
    if pounds_of_pasta % 3 != 0:
        racks_needed += 1

    # Calculate the number of additional racks needed
    additional_racks_needed = racks_needed - 3

    # Display the number of additional racks needed
    result = additional_racks_needed
    return result

print(solution())