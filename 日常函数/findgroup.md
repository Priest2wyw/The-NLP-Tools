# 根据距离分组

```python
def findGroup(lists,dist):
    '''
    目的：输入一个数字列表(从小到大排序)，返回所有距离在 `dist` 内的分组
    input: 
        list = [-5,1,2,3,4,10,11,14,18,28,31,33,80]
        dist = 4
    output:[slice(1, 5, None), slice(5, 9, None), slice(9, 12, None)]
    '''
    group = []

    start = -1
    end = -1
    for i in range(len(lists)):    
        if i < len(lists)-1:
    #         print(i,abs(n[i+1]-n[i])<4 and start <0,start,end )
            if abs(lists[i+1]-lists[i])<=dist  :
                if start <0:
                    start = i

            elif start>=0:
                end = i+1
                group.append(slice(start,end))
                start = -1
                end = -1
        elif start >=0 and end<0:
            end = i+1
            group.append(slice(start,end))
    return(group)
```

