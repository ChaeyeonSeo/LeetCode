class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # First 
        # max = 0
        # val = 0
        # hashmap = {}
        # for i, letter in enumerate(s):
        #     if ord(letter) in hashmap:
        #         if val > max:
        #             max = val
        #         num = hashmap.get(ord(letter))
        #         # print("num: ",num)
        #         for j, order in list(hashmap.items()):
        #             if order <= num:
        #                 del hashmap[j]
        #                 val -= 1
        #     hashmap[ord(letter)] = i
        #     val += 1
        #     # print(hashmap)
        #     # print(val)
        # if max < val:
        #     max = val
        # return max

        # # Second
        # chars = Counter()
        # left = right = 0
        # res = 0

        # while right < len(s):
        #     r = s[right]
        #     chars[r] += 1

        #     while chars[r] > 1:
        #         l = s[left]
        #         chars[l] -= 1
        #         left += 1

        #     res = max(res, right - left + 1)

        #     right += 1
        # return res

        # # Third
        hashmap = {}
        res = 0
        i = 0
        for j in range(len(s)):
            if s[j] in hashmap:
                i = max(hashmap[s[j]]+1, i)
            res = max(res, j - i + 1)
            hashmap[s[j]] = j
        return res
                