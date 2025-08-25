# Simplified Password Strength Analyzer & Wordlist Generator (No External Libraries)

import argparse
from datetime import datetime
import re

# Simple password strength checker (length + pattern check)
def basic_strength_check(password):
    length_score = len(password) >= 8
    complexity_score = bool(re.search(r"[A-Z]", password)) and \
                       bool(re.search(r"[a-z]", password)) and \
                       bool(re.search(r"\d", password)) and \
                       bool(re.search(r"[@#$%^&+=!*/?]", password))

    score = length_score + complexity_score
    if score == 2:
        return "Strong"
    elif length_score:
        return "Medium"
    else:
        return "Weak"

# Generate simple leetspeak variants
def leetspeak_variants(word):
    subs = {'a': ['4'], 'e': ['3'], 'i': ['1'], 'o': ['0'], 's': ['5'], 't': ['7']}
    variants = set([word])
    for i, c in enumerate(word):
        if c.lower() in subs:
            for rep in subs[c.lower()]:
                variant = word[:i] + rep + word[i+1:]
                variants.add(variant)
    return variants

# Wordlist generator
def generate_wordlist(inputs):
    base_words = set()
    for val in inputs.values():
        base_words.update(val.lower().split())

    current_year = datetime.now().year
    wordlist = set()
    for word in base_words:
        wordlist.update(leetspeak_variants(word))
        for year in range(current_year - 10, current_year + 1):
            wordlist.add(f"{word}{year}")
            wordlist.add(f"{year}{word}")

    return sorted(wordlist)

def save_wordlist(wordlist, filename):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')

def main():
    parser = argparse.ArgumentParser(description="Simple Password Analyzer & Wordlist Generator")
    parser.add_argument("--password", required=True, help="Password to check")
    parser.add_argument("--name", help="Name input")
    parser.add_argument("--date", help="Date input")
    parser.add_argument("--pet", help="Pet name input")
    parser.add_argument("--output", default="simple_wordlist.txt", help="Output file")
    args = parser.parse_args()

    # Strength check
    strength = basic_strength_check(args.password)
    print("Password Strength:", strength)

    # Wordlist generation
    inputs = {
        'name': args.name or '',
        'date': args.date or '',
        'pet': args.pet or ''
    }
    wordlist = generate_wordlist(inputs)
    save_wordlist(wordlist, args.output)
    print(f"Wordlist saved to {args.output} with {len(wordlist)} entries.")

if __name__ == "__main__":
    main()