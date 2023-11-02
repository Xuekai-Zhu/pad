def solution():
    """Henry has 30 more lollipops than Alison does. With 60 lollipops, Alisson has half the number of lollipops Diane has. If they combine the lollipops and eat 45 lollipops each day, calculate the total number of days it will take for them to finish the lollipops."""
    # Calculate the number of lollipops Alison has
    a_lollipops = 60

    # Calculate the number of lollipops Henry has
    h_lollipops = a_lollipops + 30

    # Calculate the total number of lollipops
    total_lollipops = a_lollipops + h_lollipops

    # Calculate the number of lollipops Diane has
    d_lollipops = 2 * a_lollipops

    # Calculate the total number of lollipops
    total_lollipops += d_lollipops

    # Calculate the number of days it will take to finish the lollipops
    days = total_lollipops // (45 * 3)

    # Display the number of days
    result = days
    return result

print(solution())