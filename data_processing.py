import csv, os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, "Cities.csv")) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


def filter_items(condition, dict_list):
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)


avg_func = lambda vals: sum(float(v) for v in vals) / len(vals)

# Print first 5 cities only
for city in cities[:5]:
    print(city)
print()

# Print the average temperature of all the cities
avg_temp_all = aggregate("temperature", avg_func, cities)
print("Average temperature of all cities:", avg_temp_all)
print()

# Print all cities in Germany

print("All cities in Germany:")
Germany_cities = filter_items(lambda c: c["country"] == "Germany", cities)
print("Cities in Germany:", [c["city"] for c in Germany_cities])
print()

# Print all cities in Spain with a temperature above 12°C

spain_warm_cities = filter_items(
    lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12, cities
)
print("Cities in Spain with temp > 12°C:", [c["city"] for c in spain_warm_cities])
print()

# Count the number of unique countries

unique_countries_count = aggregate(
    "country", lambda countries: len(set(countries)), cities
)
print("Number of unique countries:", unique_countries_count)
print()

# Print the average temperature for all the cities in Germany

avg_temp_germany = aggregate("temperature", avg_func, Germany_cities)
print("Average temperature in Germany:", avg_temp_germany)
print()

# Print the max temperature for all the cities in Italy

Italy_cites = filter_items(lambda c: c["country"] == "Italy", cities)
max_temp_italy = aggregate(
    "temperature", lambda vals: max(float(v) for v in vals), Italy_cites
)
print("Max temperature in Italy:", max_temp_italy)
