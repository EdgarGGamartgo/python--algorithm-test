from typing import Dict


def badCharHeuristic(string, size):
    badChar = [-1]*256
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern

    def search(self) -> int:
        m = len(self.pattern)
        n = len(self.text)

        badChar = badCharHeuristic(self.pattern, m)

        s = 0
        while(s <= n-m):
            j = m-1

            while j >= 0 and self.pattern[j] == self.text[s+j]:
                j -= 1

            if j < 0:
                return s
            else:
                s += max(1, j-badChar[ord(self.text[s+j])])
        return -1
