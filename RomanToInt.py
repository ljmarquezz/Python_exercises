class Solution(object):
    def romanToInt(self, s):
        symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        values = list(map(lambda x:symbols[x], s))
        values.reverse()
        prev_value=0
        total=0
        for number in values:
            if number < prev_value:
                total -= number
            else:
                total += number
            prev_value=number
        return total