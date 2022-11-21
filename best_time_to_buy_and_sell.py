def maxProfit(prices):
    n=len(prices)
    buy=0
    dp=[[-1]*2 for i in range(n+1)]
    dp[n][0]=0
    for ind in range(n-1,-1,-1):
        for buy in range(0,2):
            if buy==0:
                dp[ind][buy]=max((-prices[ind]+dp[ind+1][1]),(dp[ind+1])[0])
            else:
                dp[ind][buy]=max((+prices[ind]+dp[ind+1][0]),(dp[ind+1])[1])
    return dp[0][0]

# [7,1,5,3,6,4]
l=list(map(int,input().split()))
print(maxProfit(l))