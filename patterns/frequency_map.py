# Anagrams 
'''Given 2 strings, write a function to determine 
if the second string is an anagram of the first. An anagram is a word, phrase, or name formed by rearranging the letter of another, such as
cinema, formed from iceman'''


'''input [cinema, iceman] o
Output True'''


# 2 wAYS TO SOLVE IT

def is_anagram_a(a,b):
    if len(a) != len(b):
        return False

    freq_map_a = {}
    freq_map_b = {}

    for item in a:
        if item in freq_map_a:
            freq_map_a[item] += 1
        else:
            freq_map_a[item] =0

    for item in b:
        if item in freq_map_b:
            freq_map_b[item] += 1
        else:
            freq_map_b[item] =0

    if freq_map_b == freq_map_a:
        return True
    return False

a = 'cat'
b='cat'
print(is_anagram_a(a,b))

def is_anagram_b(a,b):
    if len(a) != len(b):
        return False

    freq_map_a = {}


    for item in a:
        if item in freq_map_a:
            freq_map_a[item] += 1
        else:
            freq_map_a[item] =1

    for item in b:
        if freq_map_a[item] == 0:
            return False
        else:
            freq_map_a[item] -= 1

    return True

print(is_anagram_b(a,b))