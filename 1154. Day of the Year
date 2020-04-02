class Solution:
    def dayOfYear(self, date: str) -> int:
        days = 0
        a = date.split('-')
        md = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (int(a[0]) % 4) == 0:
            if (int(a[0]) % 100) == 0:
                   if (int(a[0]) % 400) == 0:
                           md[1]=29
            else:
                   md[1]=29
        for i in range(0,int(a[1])-1):
            days = days + md[i]
            print(days)
        return days + int(a[2])
