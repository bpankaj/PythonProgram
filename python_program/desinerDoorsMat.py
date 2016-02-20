#import sys
#if sys.version_info[0]>=3: raw_input=input
N,M=map(int,raw_input().split())
#a=[('.|.'*i).center(M,'-') for i in range(1,N,2)]
#for e in a+['WELCOME'.center(M,'-')]+list(reversed(a)):print(e)

for i in range(1, N, 2):
	print ('.|.' * i).center(M, '-')
print "WELCOME".center(M, '-')
for i in range(N-2, -1, -2):
	print ('.|.'*i).center(M, '-')
