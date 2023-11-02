def solution():
    """After trick-or-treating, Brent dumped his candy on the table. He had received 5 Kit-Kat bars, three times that amount in Hershey kisses, 8 boxes of Nerds, and 11 lollipops. He also had 10 Baby Ruths and half that amount in Reese Peanut butter cups. After giving his little sister 5 lollipops, how many pieces of candy did Brent have left?"""
    # Define the initial number of candies
    candies = 0

    # Calculate the total number of candies
    candies += 5  # Kit-Kat bars
    candies += 3 * 5  # Hershey kisses (3 times the number of Kit-Kat bars)
    candies += 8  # Nerds
    candies += 11  # lollipops
    candies += 10  # Baby Ruths
    candies += 0.5 * 10  # Reese Peanut butter cups (half the number of Baby Ruths)

    # Subtract the candies given to Brent's sister
    candies -= 5

    # Return the remaining candies
    result = candies
    return result

print(solution())