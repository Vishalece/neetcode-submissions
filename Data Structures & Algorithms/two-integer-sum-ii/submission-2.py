class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers)-1
        value = 0
        while(e >= s):
            value = (numbers[s]+numbers[e])
            if( value == target):
                return [s+1,e+1]
            elif (value > target):
                e =e -1
            elif(value < target) :
                s =s +1

        