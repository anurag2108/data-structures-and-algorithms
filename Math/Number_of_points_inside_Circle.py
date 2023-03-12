class Solution:
    def calDistance(self,p1,p2):
        x1,y1,x2,y2 = p1[0],p1[1],p2[0],p2[1]
        return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    
    #Based on the queries calculating the distance with each point and checking if the distance 
    #is less than or equal to the radius.
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answers=[]
        for i in queries:
            x,y,r = i[0],i[1],i[2]
            count = 0
            for j in points:
                if(self.calDistance(j,[x,y])<=r):
                    count+=1
            answers.append(count)
        return answers