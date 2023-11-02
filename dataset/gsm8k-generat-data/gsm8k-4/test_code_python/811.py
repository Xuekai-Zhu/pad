def solution():
    """Steve owns a lake shop that sells fish. He has a stock of 200 fish. He sells 50 fish and because his refrigerators stop working a third of the remaining fish become spoiled. A new stock of 200 more fish arrives. How many fish does he have in stock now?"""
    # Define the initial number of fish
    initial_fish = 200

    # Calculate the number of fish sold
    fish_sold = 50

    # Calculate the number of fish that become spoiled
    fish_spoiled = int((initial_fish - fish_sold) / 3)

    # Calculate the number of fish remaining after selling and spoilage
    remaining_fish = initial_fish - fish_sold - fish_spoiled

    # Add the new stock of fish
    new_stock = 200

    # Calculate the total number of fish on hand
    total_fish = remaining_fish + new_stock

    # return the result
    result = total_fish
    return result

print(solution())