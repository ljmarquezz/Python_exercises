def letterCombinations(digits):
    if len(digits)>4:
        return []
    if not digits:
        return []
    digits_num = []
    combinations = []
    for digit in digits:
        if int(digit) not in range(2,10):
            return []
        digits_num.append(int(digit))
    buttons = {
        2: ['a','b','c'],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m','n','o'],
        7: ['p','q','r','s'],
        8: ['t','u','v'],
        9: ['w','x','y', 'z'],
    }

    def helper(index, current_string):
        if index == len(digits_num):
            combinations.append(current_string)
        else:
            for letter in buttons[digits_num[index]]:
                helper(index+1, current_string+letter)
        
    helper(0, '')

    return combinations

if __name__ == '__main__':
    phone = '4673'
    print (letterCombinations(phone))

