class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            counter = [0] * 26
            for char in s:
                counter[ord(char) - ord("a")] += 1

            counter = tuple(counter)

            if counter in hashmap:
                hashmap[counter].append(s)
            else:
                hashmap[counter] = [s]

        return hashmap.values()
