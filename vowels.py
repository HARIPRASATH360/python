text = "HARI PRASATH"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"Total vowels: {vowel_count}")