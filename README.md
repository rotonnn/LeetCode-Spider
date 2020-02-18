# LeetCode Spider
 LeetCode爬虫，可以爬取AC题目的 标题、题目内容、最近通过代码
 
#spider.py 
包含函数 login4cookies ，用于登录并返回登录状态的所有cookies。
根据提示输入登录所需的用户名和密码。

#s_spider.py
根据提示输入需要爬取题库的url，
等待爬取完毕，结果将以json形式输出在文件夹下的`data.json`中。

输出形式：
```json
{"title": "两数之和", "link": "https://leetcode-cn.com/problems/two-sum", "content": "给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。示例:", "code": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        ind=[i for i in range(len(nums))]\n        temp=sorted(zip(nums,ind))\n        nums=[i[0] for i in temp]\n        ind=[i[1] for i in temp]\n        l,r=0,len(nums)-1\n        cal=nums[0]+nums[-1]\n        minus=abs(cal-target)\n        res=[ind[l],ind[r]]\n        while l<r:\n            if cal<target:\n                l+=1\n            elif cal>target:\n                r-=1\n            else:\n                return res\n            cal=nums[r]+nums[l]\n            if abs(cal-target)<=minus:\n                minus=abs(cal-target)\n               \n                res=[ind[l],ind[r]]\n           \n        return res\n"}
```