class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums=list(int(input("Enter the list: ")))
        seen=set()
        for i in nums:
            if i in seen:
                print(True)
                break
                seen.add(i)
            else:
                print(False)