class Solution:
    #Reference - https://www.youtube.com/watch?v=q6IEA26hvXc , https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
    #Time Complexity - O(min(logM,logN))
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        n,m= len(nums1),len(nums2)
        
        if(n>m):
            return self.findMedianSortedArrays(nums2,nums1)
        
        midind = (n+m+1)//2
        l,r = 0,n

        while l<=r:
            mid = (l+r)//2
            firstpart = mid
            secondpart = midind - mid

            Aleft = nums1[firstpart-1] if(firstpart>0) else float("-inf")
            Aright = nums1[firstpart] if(firstpart<n) else float("inf")
            
            Bleft = nums2[secondpart-1] if(secondpart>0) else float("-inf")
            Bright = nums2[secondpart] if(secondpart<m) else float("inf")

            if(Aleft<=Bright and Bleft<=Aright):
                #odd
                if((n+m)%2):
                    return max(Aleft,Bleft)
                #even
                return (max(Aleft,Bleft) + min(Aright,Bright))/2
            
            elif(Aleft>Bright):
                r = firstpart-1
            
            else:
                l = firstpart+1