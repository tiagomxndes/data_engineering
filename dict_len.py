"""
Exercise 3 — Dictionaries
Write a function count_word_lengths(words) that:
Takes a list of strings
Returns a dictionary mapping each word length (int) to how many words in the list have that length
Example: count_word_lengths(["cat", "dog", "fish", "ox"]) → {3: 2, 4: 1, 2: 1}
"""


def count_word_lengths(words: list[str]) -> dict:

    if not words:
        return {}

    len_words = [len(word) for word in words]  # [3, 3, 4, 2]
    dict_len = {}

    for len_word in len_words:
        if len_word not in dict_len:
            dict_len[len_word] = 0
        dict_len[len_word] += 1

    return dict_len


print(count_word_lengths(["cat", "dog", "fish", "ox"]))
