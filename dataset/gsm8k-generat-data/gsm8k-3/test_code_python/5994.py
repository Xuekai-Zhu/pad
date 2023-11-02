def solution():
    """Dani has 3 cats; Binkie, Frankie and Spaatz.  Each cat has a collar decorated with gemstones.  Binkie has four times as many gemstones on his collar as does Frankie but Spaatz has two less than half as many gemstones on her collar as does Frankie.  If Spaatz has 1 Gemstone on her collar, how many gemstones does Binkie have on his collar?"""
    # Define the number of gemstones on Spaatz's collar
    spaatz_gems = 1

    # Calculate the number of gemstones on Frankie's collar
    frankie_gems = (spaatz_gems + 2) * 2

    # Calculate the number of gemstones on Binkie's collar
    binkie_gems = frankie_gems * 4

    # Display the number of gemstones on Binkie's collar
    result = binkie_gems
    return result

print(solution())