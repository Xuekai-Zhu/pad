def solution():
    """Erica is telling her grandson about the animals she saw during her recent safari in Kenya's Maasai Mara. On Saturday, she saw 3 lions and 2 elephants. She spotted 2 buffaloes and 5 leopards on Sunday, and 5 rhinos and 3 warthogs on Monday. What is the total number of animals that Erica saw?"""
    # Define the number of animals seen on each day
    saturday_animals = 3 + 2
    sunday_animals = 2 + 5
    monday_animals = 5 + 3

    # Calculate the total number of animals seen
    total_animals = saturday_animals + sunday_animals + monday_animals

    # return the result
    result = total_animals
    return result

print(solution())