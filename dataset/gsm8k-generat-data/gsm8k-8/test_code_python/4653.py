def solution():
    # Define the amount of cans Rachel brought in
    rachel_cans = None

    # Calculate the amount of cans Jaydon brought in
    jaydon_cans = 2 * rachel_cans + 5

    # Calculate the amount of cans Mark brought in
    mark_cans = 4 * jaydon_cans

    # Calculate the total amount of cans
    total_cans = rachel_cans + jaydon_cans + mark_cans

    # Solve for the value of rachel_cans
    rachel_cans = (135 - mark_cans - jaydon_cans) // 3

    # Return the amount of cans Mark brought in
    result = mark_cans
    return result

print(solution())