class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums=list(int(input("Enter the list: ").split()))
        seen=set()
        for i in nums:
            if i in seen:
                print(True)
                seen.add(i)
                break
            else:
                print(False)