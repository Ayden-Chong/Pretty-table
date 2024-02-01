from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['#', 'Pokemon Name']
# pokemonnumber = ["001", "002", "003", "004", "005", "006", "007", "008", "009"]
# pokemonname = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
#         "Squirtle", "Wartortle", "Blastoise", "Caterpie"]

table.add_rows("001", "Bulbasaur")
table.add_rows("002", "Ivysaur")
table.add_rows("004", "Venusaur")
table.add_rows("005", "Charmander")
table.add_rows("006", "Charmeleon")
table.add_rows("007", "Charizard")
table.add_rows("008", "Squirtle")
table.add_rows("009", "Wartortle")
table.add_rows("0010", "Blastoise")
table.add_rows("0011", "Caterpie")

print(table)
