class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)) :
            return False
        # for i in s :
        #     if((i not in t)):
        #         return False
        #     elif ((s.count(i) != t.count(i))):
        #         return False
        # return True
        # for i in s :
        #     if ((s.count(i) != t.count(i))):
        #         return False
        # return True
        m1={}
        m2={}

        for i in s :
            if i in m1:
                m1[i]+=1
            else :
                m1[i]=1

        for j in t :
            if j in m2:
                m2[j]+=1
            else :
                m2[j]=1

        return m1==m2



        