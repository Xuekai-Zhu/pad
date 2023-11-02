def solution():
    # Define the number of family members joining
    num_members = 4

    # Calculate the total cost for one person for one year
    yearly_cost_per_person = 4000 + 12 * 1000

    # Calculate the total cost for John and his family for one year
    total_cost = num_members * yearly_cost_per_person

    # Calculate how much John needs to pay, which is half the total cost
    john_payment = total_cost / 2
    result = john_payment
    return result

print(solution())