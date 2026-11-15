class Solution:

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0) :
            return ""
        s = ""
        for i in strs:
            s+= str(len(i))+"#"+i
        return s

            


    def decode(self, s: str) -> List[str]:
        # l = s.split("@")
        # l.pop()
        # for i in range(len(l)):
        #     l[i] = l[i][1:]
        # return l
        #5#hello5#world
        l=[]
        i , j = 0, 0
        while(i<len(s)) : #14
            j = i #0
            # if(s[j] != '#') :
            #     j = j+1
            while(s[j] != '#') :
                j+=1
            length = int(s[i:j]) #5 
            l.append(s[j+1 : j+1+length]) #hello
            i = j+1+length 
        return l


