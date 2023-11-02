def solution():
    """Five friends eat at a fast-food chain and order the following: 5 pieces of hamburger that cost $3 each; 4 sets of French fries that cost $1.20; 5 cups of soda that cost $0.5 each; and 1 platter of spaghetti that cost $2.7. How much will each of them pay if they will split the bill equally?"""
    hamburgers = 5 * 3
    french_fries = 4 * 1.2
    soda = 5 * 0.5
    spaghetti = 2.7
    total_bill = hamburgers + french_fries + soda + spaghetti
    bill_per_person = total_bill / 5
    result = bill_per_person
    return result

print(solution())