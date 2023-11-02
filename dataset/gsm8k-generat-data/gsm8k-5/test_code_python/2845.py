def solution():
    blood_per_mosquito = 20  # A mosquito sucks 20 drops of blood
    drops_per_liter = 5000  # There are 5000 drops per liter of blood
    liters_to_die = 3  # You have to lose 3 liters of blood to die

    # Calculate the total number of drops of blood you need to lose to die
    total_drops_to_die = liters_to_die * drops_per_liter

    # Calculate the number of mosquitoes required to suck enough blood to kill you
    mosquitoes_to_die = total_drops_to_die / blood_per_mosquito
    result = mosquitoes_to_die
    return result

print(solution())