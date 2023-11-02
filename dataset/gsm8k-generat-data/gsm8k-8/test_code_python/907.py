def solution():
    # Define the total number of pallets received
    total_pallets = 20

    # Calculate the number of pallets for each type of paper product
    paper_towels = total_pallets / 2
    tissues = total_pallets / 4
    paper_plates = total_pallets / 5

    # Calculate the number of pallets for paper cups
    paper_cups = total_pallets - (paper_towels + tissues + paper_plates)

    result = paper_cups
    return result

print(solution())