def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    if "" in strs:
        return ""
    prev_word=""
    CommonPrefix=""
    for word in strs:
        if prev_word:
            prefix = ""
            for (x, y) in zip(prev_word, word):
                if x == y:
                    prefix += x
                else:
                    break
            if CommonPrefix and prefix:
                NewCommonPrefix=""
                for (x, y) in zip(CommonPrefix, prefix):
                    NewCommonPrefix += x
                CommonPrefix = NewCommonPrefix
            elif prefix:
                CommonPrefix=prefix
            else:
                return ""
        prev_word = word
    return CommonPrefix

words = ["","cbc","c","ca"]

print(longestCommonPrefix(words))