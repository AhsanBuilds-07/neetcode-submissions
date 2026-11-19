from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count=Counter(nums)
        result=count.most_common(k)
        # most_common=
        ans=[]
        for nums,frequency in result:
            ans.append(nums)
        return ans