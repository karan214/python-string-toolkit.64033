def count_exclamations(text):
    """RETURN NO OF EXCLAMATIONS MARKS IN A TEXT"""
    count = 0

    for char in text:
        if char == '!':
            count += 1

    return count


text = input("Enter a text: ")

result = count_exclamations(text)

print("Count:", result)
