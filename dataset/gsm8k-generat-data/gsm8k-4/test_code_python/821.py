def solution():
    """Sammy can eat 15 pickle slices. His twin sister Tammy can eat twice as much as Sammy. Their older brother Ron eats 20% fewer pickles slices than Tammy. How many pickle slices does Ron eat?"""
    # Define the number of pickle slices Sammy can eat
    sammy_slices = 15

    # Calculate the number of pickle slices Tammy can eat
    tammy_slices = 2 * sammy_slices

    # Calculate the percentage reduction for Ron
    reduction = 0.2

    # Calculate the number of pickle slices Ron can eat
    ron_slices = tammy_slices - (tammy_slices * reduction)

    result = ron_slices
    return result

print(solution())