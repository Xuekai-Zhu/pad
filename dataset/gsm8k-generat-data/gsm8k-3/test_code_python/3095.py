def solution():
    """In a Zoo, there are different animals. There are 5 giraffes and twice as many penguins. Penguins make up 20% of all the animals in the Zoo. How many elephants are there in the Zoo if they make up 4% of all the animals?"""
    # Calculate the total number of animals in the Zoo
    penguin_percent = 20
    penguin_factor = 100 / penguin_percent
    total_animals = 5 + (2 * penguin_factor * 5)

    # Calculate the number of elephants in the Zoo
    elephant_percent = 4
    elephant_factor = 100 / elephant_percent
    elephant_count = elephant_factor / total_animals

    # Display the number of elephants
    result = elephant_count
    return result

print(solution())