def solution():
    """Quentavious has 5 nickels. His friend offers him some gum and will give him two pieces per nickel. If Quentavious leaves with 2 nickels, how many pieces of gum did he get?"""
    initial_nickels = 5
    final_nickels = 2
    gum_per_nickel = 2
    nickels_used = initial_nickels - final_nickels
    gum_received = nickels_used * gum_per_nickel
    result = gum_received
    return result

print(solution())