def solution():
    """Keanu's motorcycle can store 8 liters of gasoline. If his destination is 280 miles away and his motorcycle consumes 8 liters of gasoline per 40 miles, how many times does Keanu have to refill his motorcycle with gasoline if he will make a round trip?"""
    # Define the capacity of Keanu's motorcycle tank and the fuel consumption per mile
    capacity = 8
    consumption = 0.2  # 8 liters per 40 miles

    # Calculate the total distance of the round trip
    total_distance = 2 * 280  # round trip

    # Calculate the total fuel needed for the round trip
    total_fuel = total_distance * consumption

    # Calculate the number of times Keanu needs to refill his motorcycle
    num_refills = total_fuel / capacity

    # Round up the number of refills to the nearest integer
    num_refills = int(num_refills) if num_refills.is_integer() else int(num_refills) + 1

    result = num_refills
    return result

print(solution())