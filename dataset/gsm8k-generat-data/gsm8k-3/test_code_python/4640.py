def solution():
    """Teresa is collecting pencils. She has 14 colored pencils and 35 black pencils. Her three younger siblings need pencils for class and their dad asks her to share all her pencils, giving each an equal number of pencils, regardless of color. He tells her she can keep 10 of them for herself. How many pencils does each sibling get?"""
    # Define the number of colored and black pencils Teresa has
    colored_pencils = 14
    black_pencils = 35

    # Calculate the total number of pencils Teresa has
    total_pencils = colored_pencils + black_pencils

    # Calculate the number of pencils Teresa will keep
    keep_pencils = 10

    # Calculate the total number of pencils Teresa will give to her siblings
    give_pencils = total_pencils - keep_pencils

    # Calculate the number of pencils each sibling will get
    sibling_pencils = give_pencils / 3

    # Display the number of pencils each sibling will get
    result = sibling_pencils
    return result

print(solution())