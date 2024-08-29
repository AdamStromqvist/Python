class Solution(object):
    def twoSums(self, nums, target):
        seen = {}  # Skapar ett tomt dictionary som ska hålla koll på tidigare tal och deras index.

        for i, num in enumerate(nums):  # Loopar igenom listan nums, där i är indexet och num är värdet på det nuvarande talet.
            # Kollar om skillnaden mellan target och det aktuella talet (num) finns i dictionaryt seen.
            # Detta innebär att vi letar efter ett tidigare sett tal som tillsammans med num blir lika med target.
            if target - num in seen:  
                # Om vi hittar en match (ett tal som kan kombineras med det aktuella num för att bli target),
                # returnerar vi en lista med indexet för det tidigare talet (hämtat från seen) och det aktuella indexet (i).
                return [seen[target - num], i]
            # Om det aktuella talet (num) inte finns i seen, lägg till det i dictionaryt med sitt index.
            elif num not in seen:  
                seen[num] = i  # Lagrar det aktuella talet som nyckel och dess index som värde i seen.

# Testfall
nums = [2, 7, 11, 15]  # Lista med tal
target = 9  # Målvärdet vi vill uppnå genom att summera två tal från listan

# Skapa en instans av Solution och kör metoden twoSums
solution = Solution()
result = solution.twoSums(nums, target)

print(f"Indicies för tal som summeras till {target} är: {result}")
