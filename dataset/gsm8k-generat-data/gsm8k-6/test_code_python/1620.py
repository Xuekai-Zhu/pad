def solution():
    # Calculate the amount of pasta dough Michelle can make with 3 bags of flour
    dough = 2 * 3 * 8  # each bag of flour makes 2 pounds of dough, and it takes 2 cups of flour to make 1 pound of dough

    # Calculate the number of drying racks Michelle needs for the dough
    racks_needed = dough // 3  # Michelle needs one drying rack for each 3 pounds of pasta

    # Calculate the number of additional drying racks Michelle needs
    additional_racks_needed = racks_needed - 3  # Michelle currently owns 3 racks

    result = additional_racks_needed
    return result

print(solution())