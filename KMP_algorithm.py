def KMP(pattern, text):
    def compute_prefix_function(pattern):
        prefix = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = prefix[j-1]
            if pattern[j] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix

    prefix = compute_prefix_function(pattern)
    q = 0
    for i in range(len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = prefix[q-1]
        if pattern[q] == text[i]:
            q += 1
        if q == len(pattern):
            return i - (q - 1)
    return -1