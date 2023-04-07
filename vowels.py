def combine_strings(s1, s2):
    combined = ""
    for i in range(max(len(s1), len(s2))):
        if i < len(s1):
            combined += s1[i]
        if i < len(s2):
            combined += s2[i]
    return combined
def reverse_alternate(s):
    words = s.split()
    for i in range(len(words)):
        if i % 2 == 1:
            words[i] = words[i][::-1]
    return " ".join(words)
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
s3 = combine_strings(s1, s2)
print("Combined string: " + s3)
s3_reversed = reverse_alternate(s3)
print("Reverse alternate words in string: " + s3_reversed)
vowel_count = count_vowels(s3_reversed)
print("Vowel count in string: " + str(vowel_count))
