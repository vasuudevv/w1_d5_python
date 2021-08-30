population = {
    "Mumbai": 1000097000,
    "Delhi": 100030456,
    "Jaipur": 4067826,
    "Banglore": 29849742,
    "Pune": 6807984
}

def most_populated(name):
    return max(zip(population.values(), Tv.keys()))[1]

def city_population(name):
    return population[name]

def all_cities():
    return list(population.keys())