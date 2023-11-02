def solution():
    contestants = 18
    female_contestants = contestants / 3
    male_contestants = contestants - female_contestants
    result = male_contestants
    return result
    

Question: A cash register contains $100 in twenties and receives $50 in twenties as a customer’s payment. How many twenties are in the register now?

Solution:
def solution():
    twenties_in_register = 100
    twenties_received = 50
    twenties_total = twenties_in_register + twenties_received
    result = twenties_total
    return result

print(solution())