class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            beginIndex1, beginIndex2 = 0, 0
            while True:
                # nums1 done, select kth from nums2
                if beginIndex1 == m:
                    return nums2[beginIndex2 + k - 1]
                # nums2 done, select kth from nums1
                if beginIndex2 == n:
                    return nums1[beginIndex1 + k - 1]
                # last element to get
                if k == 1:
                    return min(nums1[beginIndex1], nums2[beginIndex2])

                # pI1 within median of current nums1 to end
                pivotIndex1 = min(beginIndex1 + k//2 - 1, m - 1)
                # pI2 within median of current nums2 to end
                pivotIndex2 = min(beginIndex2 + k//2 - 1, n - 1)

                pivot1 = nums1[pivotIndex1]
                pivot2 = nums2[pivotIndex2]

                # compare p1 and p2, if p1 is smaller
                if pivot1 <= pivot2:
                    # k set to half - 1
                    k -= pivotIndex1 - beginIndex1 + 1
                    # skip p1, look into second half of current nums1
                    beginIndex1 = pivotIndex1 + 1
                else:
                    k -= pivotIndex2 - beginIndex2 + 1
                    beginIndex2 = pivotIndex2 + 1

        m, n = len(nums1), len(nums2)
        length = m + n
        # odd length
        if length % 2 == 1:
            return getKthElement(length//2 + 1)
        # even length
        else:
            return (getKthElement(length//2) + getKthElement(length//2 + 1)) / 2

# test cases
nums1 = [1,2]
nums2 = [3,4]
out = 2.5
