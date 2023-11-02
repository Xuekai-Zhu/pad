def solution():
    """Quentavious has 5 nickels. His friend offers him some gum and will give him two pieces per nickel. If Quentavious leaves with 2 nickels, how many pieces of gum did he get?"""
    # Define the number of nickels Quentavious has
    num_nickels = 5

    # Define the number of pieces of gum per nickel
    gum_per_nickel = 2

    # Calculate the total number of pieces of gum Quentavious can get
    total_gum = num_nickels * gum_per_nickel

    # Calculate the number of pieces of gum Quentavious ends up with, after leaving with 2 nickels
    gum_left = (num_nickels - 2) * gum_per_nickel

    # Display the number of pieces of gum Quentavious got
    result = gum_left
    return result

print(solution())