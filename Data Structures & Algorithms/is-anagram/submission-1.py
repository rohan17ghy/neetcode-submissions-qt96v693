class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = (s, t) if len(s) > len(t) else (t, s)
        sCount = collections.Counter(s)
        
        #Instead of iterating t we can create another counter for t string
        #and compare it directly with the counter s
        #Reducing one counter of t
        for char in t:
            if char in sCount and sCount[char] > 0:
                sCount[char] -= 1
            
            #delete empty keys
            if char in sCount and sCount[char] == 0:
                sCount.pop(char, None)

        print(sCount)
        
        return len(sCount) == 0
        