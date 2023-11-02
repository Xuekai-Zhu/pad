def solution():
    """Quentavious has 5 nickels. His friend offers him some gum and will give him two pieces per nickel. If Quentavious leaves with 2 nickels, how many pieces of gum did he get?"""
    # Define the number of nickels Quentavious has and the number he leaves with
    initial_nickels = 5
    final_nickels = 2

    # Calculate the total number of pieces of gum Quentavious obtained
    gum_pieces = (initial_nickels - final_nickels) * 2

    # return the result
    result = gum_pieces
    return result

print(solution())