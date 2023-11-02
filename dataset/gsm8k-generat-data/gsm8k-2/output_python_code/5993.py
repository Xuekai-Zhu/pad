def solution():
    """Dani has 3 cats; Binkie, Frankie and Spaatz. Each cat has a collar decorated with gemstones. Binkie has four times as many gemstones on his collar as does Frankie but Spaatz has two less than half as many gemstones on her collar as does Frankie. If Spaatz has 1 Gemstone on her collar, how many gemstones does Binkie have on his collar?"""
    spaatz_gemstones = 1
    frankie_gemstones = (spaatz_gemstones * 2) + 2
    binkie_gemstones = frankie_gemstones * 4
    result = binkie_gemstones
    return result

print(solution())