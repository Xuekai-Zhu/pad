def solution():
    """After trick-or-treating, Brent dumped his candy on the table.  He had received 5 Kit-Kat bars, three times that amount in Hershey kisses, 8 boxes of Nerds,  and 11 lollipops.  He also had 10 Baby Ruths and half that amount in Reese Peanut butter cups.  After giving his little sister 5 lollipops, how many pieces of candy did Brent have left?"""
    # Define the number of each type of candy Brent received
    kitkat_bars = 5
    hershey_kisses = 3 * kitkat_bars
    nerds_boxes = 8
    lollipops = 11
    baby_ruths = 10
    reese_cups = 0.5 * baby_ruths

    # Calculate the total number of candies
    total_candies = kitkat_bars + hershey_kisses + nerds_boxes + lollipops + baby_ruths + reese_cups

    # Subtract the candies given to Brent's sister
    total_candies -= 5

    # Display the number of candies left
    result = total_candies
    return result

print(solution())