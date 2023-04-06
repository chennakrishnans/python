def length_of_last_word(s):
    s = s.strip()
    words = s.split()
    if not words:
        return 0
    return len(words[-1])
s = input("Enter a string: ")
print("Length of the last word:", length_of_last_word(s))
