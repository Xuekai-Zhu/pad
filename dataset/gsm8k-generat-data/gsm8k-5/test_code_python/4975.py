def solution():
    collection_size = 24  # Angela has a collection of 24 rare action figures

    # Calculate the number of action figures Angela sold at the pawnshop
    sold_figures = collection_size // 4

    # Calculate the remainder after selling a quarter of the collection
    remaining_figures = collection_size - sold_figures

    # Calculate the number of action figures Angela gave to her daughter
    given_figures = remaining_figures // 3

    # Calculate the number of action figures Angela has left
    remaining_figures -= given_figures

    result = remaining_figures
    return result

print(solution())