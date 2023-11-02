def solution():
    """Pete and Raymond each receive $2.50 from their grandmother. Pete saves his money and only spends 4 nickels. Raymond spends his money at the arcade games but still has 7 dimes left. How much did Pete and Raymond spent altogether, in cents?"""
    # Define the amount of money each received in cents
    pete_money = 250
    raymond_money = 250

    # Calculate how much Pete spent
    pete_spent = 4 * 5

    # Calculate how much Raymond spent
    raymond_spent = raymond_money - 10 * 7

    # Calculate the total amount spent
    total_spent = pete_spent + raymond_spent

    return total_spent

The solution returned by the code is incorrect because the question asks for the total amount SPENT by both Pete and Raymond, not the total amount they have left. To fix the code, we need to subtract the amount that Raymond has left from the amount he received, and then add that to the amount that Pete spent. 

Here's the corrected code:

def solution():
    """Pete and Raymond each receive $2.50 from their grandmother. Pete saves his money and only spends 4 nickels. Raymond spends his money at the arcade games but still has 7 dimes left. How much did Pete and Raymond spent altogether, in cents?"""
    # Define the amount of money each received in cents
    pete_money = 250
    raymond_money = 250

    # Calculate how much Pete spent
    pete_spent = 4 * 5

    # Calculate how much Raymond spent
    raymond_spent = raymond_money - (10 * 7 + 5)  # subtracting the amount he has left

    # Calculate the total amount spent
    total_spent = pete_spent + raymond_spent

    return total_spent

print(solution())