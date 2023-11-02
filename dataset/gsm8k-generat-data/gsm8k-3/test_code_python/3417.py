def solution():
    """Melly's two cats each have litters of kittens at the same time. The first cat has 3 blue-eyed kittens and 7 brown-eyed kittens. The second cat has 4 blue-eyed kittens and 6 brown-eyed kittens. What percentage of all the kittens have blue eyes?"""
    # Define the number of blue-eyed and brown-eyed kittens for each cat
    cat1_blue = 3
    cat1_brown = 7
    cat2_blue = 4
    cat2_brown = 6

    # Calculate the total number of kittens
    total_kittens = cat1_blue + cat1_brown + cat2_blue + cat2_brown

    # Calculate the total number of blue-eyed kittens
    total_blue = cat1_blue + cat2_blue

    # Calculate the percentage of kittens with blue eyes
    percent_blue = (total_blue / total_kittens) * 100

    # Display the percentage of kittens with blue eyes
    result = percent_blue
    return result

print(solution())