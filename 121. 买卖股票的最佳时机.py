class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==[]:
            return 0
        tmp=0
        buy=prices[0]
        for i in prices:
            if i-buy>tmp:#i天卖出利润更高,更新当前最大利润
                tmp=i-buy
            elif i-buy<0:#i天比上一次买入价格还低,更新买入价格
                buy=i
        return tmp

s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([9,2,4,5,7,5,3,7]))
