import csv
from fuzzywuzzy import fuzz

def load_valid_symbols(csv_file):
    
    valid_symbols = []
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            valid_symbols.append(row["Symbol"])
    return valid_symbols

def find_similar_symbols(symbol, valid_symbols):
  
    similarity_scores = {s: fuzz.ratio(symbol.upper(), s.upper()) for s in valid_symbols}
    best_matches = sorted(similarity_scores.items(), key=lambda item: item[1], reverse=True)[:5]
    return best_matches

print(find_similar_symbols("apple", load_valid_symbols('screener.csv')))