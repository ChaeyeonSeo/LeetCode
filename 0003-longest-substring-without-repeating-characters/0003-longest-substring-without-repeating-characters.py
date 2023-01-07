class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        val = 0
        hashmap = {}
        for i, letter in enumerate(s):
            if ord(letter) in hashmap:
                if val > max:
                    max = val
                num = hashmap.get(ord(letter))
                # print("num: ",num)
                for j, order in list(hashmap.items()):
                    if order <= num:
                        del hashmap[j]
                        val -= 1
            hashmap[ord(letter)] = i
            val += 1
            # print(hashmap)
            # print(val)
        if max < val:
            max = val
        return max
