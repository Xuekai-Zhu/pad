def solution():
    """There are four times as many boys at Lulu's party as girls. Each boy paid twice the money that each girl paid to attend the party.
    If there are 40 boys at the party and each boy paid $50 to attend the party, calculate the total amount of money collected at the party."""
    # Define the ratio of boys to girls
    BOYS_RATIO = 4
    GIRLS_RATIO = 1

    # Calculate the number of girls at the party
    num_boys = 40
    num_girls = num_boys//BOYS_RATIO*GIRLS_RATIO

    # Calculate the amount paid by each girl
    boy_price = 50
    girl_price = boy_price//2

    # Calculate the total amount of money collected
    total_money = num_boys*boy_price + num_girls*girl_price

    # Display the total amount of money collected
    result = total_money
    return result

print(solution())