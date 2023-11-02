def solution():
    """Half of Taylor's house guests like weak coffee and the other half like strong coffee in the morning.  Taylor uses 1 tablespoon of coffee per cup of water to make it weak and he doubles that amount to make it strong.  If he makes 12 cups of both weak and strong coffee, how many tablespoons of coffee will he need?"""
    # Calculate the total number of cups of coffee
    total_cups = 12 + 12

    # Calculate the number of tablespoons of coffee for the weak coffee
    weak_coffee_tablespoons = 1 * 12

    # Calculate the number of tablespoons of coffee for the strong coffee
    strong_coffee_tablespoons = 2 * 12

    # Calculate the total number of tablespoons of coffee
    total_tablespoons = weak_coffee_tablespoons + strong_coffee_tablespoons

    # Display the total number of tablespoons of coffee
    result = total_tablespoons
    return result

print(solution())