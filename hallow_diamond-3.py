N=int(input())
for i in range(N):
    star="* "*(N-i)
    space=" "*i
    print(star+space*4+star)
for j in range(1,N+1):
    star="* "*j
    space=" "*(N-j)
    print(star+space*4+star)
"""
input:5
output:
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
"""
