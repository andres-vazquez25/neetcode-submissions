class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        def get_frequency(item):
            return item[1]

        counts_sorted=dict(sorted(counts.items(), key=get_frequency, reverse=True))
        top_frecuency=list(counts_sorted.keys())[:k]
        return top_frecuency


