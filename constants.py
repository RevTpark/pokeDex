ALLOWED_EXTENSIONS=set(['jpg', 'jpeg', 'png'])
pokemon_types = ['Electric', 'Water', 'Psychic', 'Bug', 'Poison', 'Ghost', 'Fire', 'Fairy', 'Ground', 'Ice', 'Dragon', 'Grass', 'Flying', 'Normal', 'Rock', 'Dark', 'Steel', 'Fighting']
class_names=['Abra', 'Aerodactyl', 'Alakazam', 'Arbok', 'Arcanine', 'Articuno', 'Beedrill', 'Bellsprout', 'Blastoise', 'Bulbasaur', 'Butterfree', 'Caterpie', 'Chansey', 'Charizard', 'Charmander', 'Charmeleon', 'Clefable', 'Clefairy', 'Cloyster', 'Cubone', 'Dewgong', 'Diglett', 'Ditto', 'Dodrio', 'Doduo', 'Dragonair', 'Dragonite', 'Dratini', 'Drowzee', 'Dugtrio', 'Eevee', 'Ekans', 'Electabuzz', 'Electrode', 'Exeggcute', 'Exeggutor', 'Farfetchd', 'Fearow', 'Flareon', 'Gastly', 'Gengar', 'Geodude', 'Gloom', 'Golbat', 'Goldeen', 'Golduck', 'Golem', 'Graveler', 'Grimer', 'Growlithe', 'Gyarados', 'Haunter', 'Hitmonchan', 'Hitmonlee', 'Horsea', 'Hypno', 'Ivysaur', 'Jigglypuff', 'Jolteon', 'Jynx', 'Kabuto', 'Kabutops', 'Kadabra', 'Kakuna', 'Kangaskhan', 'Kingler', 'Koffing', 'Krabby', 'Lapras', 'Lickitung', 'Machamp', 'Machoke', 'Machop', 'Magikarp', 'Magmar', 'Magnemite', 'Magneton', 'Mankey', 'Marowak', 'Meowth', 'Metapod', 'Mew', 'Mewtwo', 'Moltres', 'MrMime', 'Muk', 'Nidoking', 'Nidoqueen', 'Nidoran_female', 'Nidoran_male', 'Nidorina', 'Nidorino', 'Ninetales', 'Oddish', 'Omanyte', 'Omastar', 'Onix', 'Paras', 'Parasect', 'Persian', 'Pidgeot', 'Pidgeotto', 'Pidgey', 'Pikachu', 'Pinsir', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Ponyta', 'Porygon', 'Primeape', 'Psyduck', 'Raichu', 'Rapidash', 'Raticate', 'Rattata', 'Rhydon', 'Rhyhorn', 'Sandshrew', 'Sandslash', 'Scyther', 'Seadra', 'Seaking', 'Seel', 'Shellder', 'Slowbro', 'Slowpoke', 'Snorlax', 'Spearow', 'Squirtle', 'Starmie', 'Staryu', 'Tangela', 'Tauros', 'Tentacool', 'Tentacruel', 'Vaporeon', 'Venomoth', 'Venonat', 'Venusaur', 'Victreebel', 'Vileplume', 'Voltorb', 'Vulpix', 'Wartortle', 'Weedle', 'Weepinbell', 'Weezing', 'Wigglytuff', 'Zapdos', 'Zubat']
mapping = {
    'Abra': 0,
    'Aerodactyl': 60,
    'Alakazam': 14,
    'Arbok': 136,
    'Arcanine': 52,
    'Articuno': 140,
    'Beedrill': 148,
    'Bellsprout': 149,
    'Blastoise': 113,
    'Bulbasaur': 139,
    'Butterfree': 81,
    'Caterpie': 80,
    'Chansey': 26,
    'Charizard': 117,
    'Charmander': 118,
    'Charmeleon': 116,
    'Clefable': 21,
    'Clefairy': 22,
    'Cloyster': 76,
    'Cubone': 77,
    'Dewgong': 109,
    'Diglett': 78,
    'Ditto': 55,
    'Dodrio': 115,
    'Doduo': 121,
    'Dragonair': 74,
    'Dragonite': 85,
    'Dratini': 84,
    'Drowzee': 95,
    'Dugtrio': 75,
    'Eevee': 42,
    'Ekans': 120,
    'Electabuzz': 32,
    'Electrode': 124,
    'Exeggcute': 82,
    'Exeggutor': 79,
    'Farfetchd': 137,
    'Fearow': 90,
    'Flareon': 44,
    'Gastly': 31,
    'Gengar': 30,
    'Geodude': 29,
    'Gloom': 96,
    'Golbat': 1,
    'Goldeen': 19,
    'Golduck': 3,
    'Golem': 18,
    'Graveler': 23,
    'Grimer': 54,
    'Growlithe': 53,
    'Gyarados': 12,
    'Haunter': 28,
    'Hitmonchan': 135,
    'Hitmonlee': 131,
    'Horsea': 94,
    'Hypno': 98,
    'Ivysaur': 130,
    'Jigglypuff': 36,
    'Jolteon': 35,
    'Jynx': 102,
    'Kabuto': 104,
    'Kabutops': 105,
    'Kadabra': 10,
    'Kakuna': 145,
    'Kangaskhan': 83,
    'Kingler': 134,
    'Koffing': 87,
    'Krabby': 119,
    'Lapras': 56,
    'Lickitung': 48,
    'Machamp': 7,
    'Machoke': 6,
    'Machop': 5,
    'Magikarp': 13,
    'Magmar': 33,
    'Magnemite': 20,
    'Magneton': 17,
    'Mankey': 103,
    'Marowak': 73,
    'Meowth': 57,
    'Metapod': 58,
    'Mew': 133,
    'Mewtwo': 132,
    'Moltres': 123,
    'Mr-mime': 46,
    'Muk': 51,
    'Nidoking': 122,
    'Nidoqueen': 125,
    'Nidoran-f': 126,
    'Nidoran-m': 127,
    'Nidorina': 128,
    'Nidorino': 129,
    'Ninetales': 27,
    'Oddish': 101,
    'Omanyte': 100,
    'Omastar': 99,
    'Onix': 50,
    'Paras': 62,
    'Parasect': 49,
    'Persian': 63,
    'Pidgeot': 143,
    'Pidgeotto': 144,
    'Pidgey': 150,
    'Pikachu': 11,
    'Pinsir': 39,
    'Poliwag': 66,
    'Poliwhirl': 69,
    'Poliwrath': 70,
    'Ponyta': 71,
    'Porygon': 45,
    'Primeape': 93,
    'Psyduck': 2,
    'Raichu': 15,
    'Rapidash': 68,
    'Raticate': 86,
    'Rattata': 88,
    'Rhydon': 67,
    'Rhyhorn': 65,
    'Sandshrew': 37,
    'Sandslash': 34,
    'Scyther': 47,
    'Seadra': 92,
    'Seaking': 16,
    'Seel': 110,
    'Shellder': 72,
    'Slowbro': 59,
    'Slowpoke': 64,
    'Snorlax': 24,
    'Spearow': 97,
    'Squirtle': 107,
    'Starmie': 41,
    'Staryu': 38,
    'Tangela': 89,
    'Tauros': 61,
    'Tentacool': 9,
    'Tentacruel': 8,
    'Vaporeon': 40,
    'Venomoth': 142,
    'Venonat': 141,
    'Venusaur': 114,
    'Victreebel': 138,
    'Vileplume': 106,
    'Voltorb': 108,
    'Vulpix': 25,
    'Wartortle': 112,
    'Weedle': 146,
    'Weepinbell': 147,
    'Weezing': 91,
    'Wigglytuff': 43,
    'Zapdos': 111,
    'Zubat': 4
}

points_mapping = {
    "attack": 1,
    "immune": 4,
    "resistant": 2,
    "defendable": 1,
    "weak": -2,
    "extremely_weak": -4,
    "weak_defense": 1,
    "extremely_weak_defense": 2
}

generations = {
    "Generation 1": "1-151",
    "Generation 2": "152-251",
    "Generation 3": "252-386",
    "Generation 4": "387-493",
    "Generation 5": "494-649",
    "Generation 6": "650-721",
    "Generation 7": "722-809"
}