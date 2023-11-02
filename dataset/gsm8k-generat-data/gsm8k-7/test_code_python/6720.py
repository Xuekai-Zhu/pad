def solution():
    starting_figures = 10
    sold_figures = 6
    upgraded_figures = 4
    brother_collection = starting_figures * 2

    # Calculate the total number of figures after selling and upgrading
    total_figures = starting_figures - sold_figures + upgraded_figures

    # Add the brother's collection to the total number of figures
    total_figures += brother_collection

    result = total_figures
    return result

print(solution())