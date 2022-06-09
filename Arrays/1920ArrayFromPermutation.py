def main():
    inp = [5,0,1,2,3,4]
    put = Solution()
    yo = put.buildArray(inp)
    print(yo)


class Solution:
    def buildArray(self, nums):
        out = []
        for index in range(len(nums)):
            out.append(nums[nums[index]])
        return out



if __name__ == '__main__':
    main()