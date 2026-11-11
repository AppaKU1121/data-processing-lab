import csv, os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, "Cities.csv")) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city["temperature"]))
print(sum(temps) / len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city["temperature"]) for city in cities]
print(sum(temps) / len(temps))
print()

# Print all cities in Germany

print("All cities in Germany:")
city_Germany = [city["city"] for city in cities if city["country"] == "Germany"]
print("Cities in Germany:", city_Germany)
print()
# Print all cities in Spain with a temperature above 12°C

Spain_warm_cities = [
    city["city"]
    for city in cities
    if city["country"] == "Spain" and float(city["temperature"]) > 12
]
print("Cities in Spain with temp > 12°C:", Spain_warm_cities)

# Count the number of unique countries

unique_countries = len(set(city["country"] for city in cities))
print("Unique countries count:", unique_countries)

# Print the average temperature for all the cities in Germany

Germany_temps = [
    float(city["temperature"]) for city in cities if city["country"] == "Germany"
]
print("Average temp in Germany:", sum(Germany_temps) / len(Germany_temps))

# Print the max temperature for all the cities in Italy

Italy_temps = [
    float(city["temperature"]) for city in cities if city["country"] == "Italy"
]
print("Max temp in Italy:", max(Italy_temps))
