class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # nums=list(int(input("Enter the list: ")))

        # nums = list(map(int, input("Enter the list: ").split())) 

        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False