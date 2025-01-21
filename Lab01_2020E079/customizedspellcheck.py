# -*- coding: utf-8 -*-
"""CustomizedSpellCheck.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FTgvnmCMKY4pZXqNGzENmYaC-6CT81_W
"""

class CustomizedSpellCheck:

    def __init__(self, word_dict_file=None):
        with open(word_dict_file, 'r') as file:
            data = file.read()
            data = data.split(",")
            data = [i.lower().strip() for i in data]
            self.dictionary = set(data)  # Using a set for faster lookups

    def check(self, string_to_check):
        self.string_to_check = string_to_check

    def levenshtein_distance(self, s1, s2):
        """Calculate the Levenshtein distance between two strings."""
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    # Heuristic-based suggestion method
    def custom_suggestions(self):
        string_words = self.string_to_check.split()
        suggestions = []

        for word in string_words:
            possible_suggestions = []

            # Go through each word in the dictionary
            for dict_word in self.dictionary:
                # Calculate the Levenshtein distance
                distance = self.levenshtein_distance(word, dict_word)

                # Calculate character overlap
                char_overlap = len(set(word) & set(dict_word))

                # Calculate length difference
                length_diff = abs(len(word) - len(dict_word))

                # Combine the scores into a final heuristic score
                score = distance - (0.5 * char_overlap) + (0.2 * length_diff)

                # Store valid suggestions with their score
                possible_suggestions.append((dict_word, score))

            # Sort suggestions by score, ascending
            possible_suggestions.sort(key=lambda x: x[1])

            # Add the top 3 suggestions to the list, ensuring no duplicates
            top_suggestions = list(dict.fromkeys([word for word, _ in possible_suggestions[:3]]))
            suggestions.append(top_suggestions)

        return suggestions