"""def runrest(N,M):
    betsy runs for 1<=n<=10,000 minutes
    each minute is running or resting
    if run: exhaustion factor must be 0 to run
        distance = D_i where i = the minute
        exhaustion factor increase by 1 but cannot exceed M
    if rest: exhaustion factor will decrease by 1
    at the end of the N minutes, exhaustion factor must be 0

    find maximal distance
    ex = 0 #exhaustion factor starts at 0
    D = 0 #total distance ran
    L = [0]*N #list of how many minutes betsy is working out

1. if N is less than or equal to 1000
2. if M = 0
3. 
"""

bestRuns = {}

def best(n):
        global bestRuns
        if n>10000:
            print "ERROR"
        elif n<=1:
            return 0
        else:
            if n in bestRuns:
                return bestRuns[n]
            
            MAX = best(n-1)
            #print "MAX at n-1 of", n-1, "is", MAX
            
            for m in range(1,M+1):
                print "m is", m
                origin = n-2*m
                if origin < 0: break
                val = best(origin)
                for j in range(0,m):
                    print "j is", j
                    val += D[origin+j]

                print "val is", val
                    
                if val > MAX:
                    MAX = val

            print "MAX at n of", n, "is", MAX

            bestRuns[n] = MAX
            return MAX
    
if __name__ == "__main__":
    
    s1 = raw_input()
    x = s1.split()
    N = int(x[0])
    M = int(x[1])
    D = [0]*N
    E = 0
    for i in range(N):
        D[i]= input()

    print best(N)
