def solution():
    num_colored_bundles = 3
    num_white_bunches = 2
    num_scrap_heaps = 5

    num_sheets_per_bundle = 2
    num_sheets_per_bunch = 4
    num_sheets_per_heap = 20

    # Calculate the total number of sheets of colored paper
    total_colored_sheets = num_colored_bundles * num_sheets_per_bundle

    # Calculate the total number of sheets of white paper
    total_white_sheets = num_white_bunches * num_sheets_per_bunch

    # Calculate the total number of sheets of scrap paper
    total_scrap_sheets = num_scrap_heaps * num_sheets_per_heap

    # Calculate the total number of sheets of paper removed from the chest of drawers
    total_sheets_removed = total_colored_sheets + total_white_sheets + total_scrap_sheets
    result = total_sheets_removed
    return result

print(solution())