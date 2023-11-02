def solution():
    """While shopping, Greg spent 300$ on a shirt and shoes. If Greg spent 9 more than twice as much on shoes as he did a shirt, how much did Greg spend on a shirt?"""
    # Define the total amount spent on the shirt and shoes
    total_spent = 300

    # Define the amount spent on shoes as a function of the amount spent on the shirt
    def shoes_spent(shirt_spent):
        return 9 + 2 * shirt_spent

    # Define the equation for the total spent
    def total_eq(shirt_spent):
        return shirt_spent + shoes_spent(shirt_spent)

    # Use a numerical solver to find the value of shirt_spent that satisfies the equation total_eq
    from scipy.optimize import fsolve
    shirt_spent = fsolve(total_eq, x0=100)[0]

    # Display the amount spent on the shirt
    result = shirt_spent
    return result

print(solution())