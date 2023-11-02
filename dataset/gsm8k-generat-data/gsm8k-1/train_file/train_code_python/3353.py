def solution():
    """Mr. Lalande inherited 20,000 euros from his old aunt Adeline. He is very happy because he will be able to afford the car of his dreams, a superb car worth 18000 €. He goes to the dealership and tries the car. He decides to take it, but instead of paying for everything right away, he chooses to pay in several installments. He pays 3,000 euros to be able to leave with the car and the seller offers to let him pay the rest in 6 monthly installments. How much does Mr. Lalande have to pay every month?"""
    total_price = 18000
    deposit = 3000
    remaining_price = total_price - deposit
    num_installments = 6
    monthly_payment = remaining_price / num_installments
    result = monthly_payment
    return result

print(solution())