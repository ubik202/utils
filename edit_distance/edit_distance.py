def edit_distance(string1,string2):
# For all i and j, d[i,j] will hold the Levenshtein distance between
# the first i characters of s and the first j characters of t.
# Note that d has (m+1) x (n+1) values.
   m = len(string1)
   n = len(string2)
   d = []
   tempd = []

   for i in range(0,n+1):
     tempd.append(0)
   for i in range(0,m+1):
     d.append(tempd[:])

   for i in range(0,m+1):
     d[i][0] = i
     # the distance of any first string to an empty second string
     # (transforming the string of the first i characters of s into
     # the empty string requires i deletions)
   for j in range(0,n+1):
     d[0][j] = j
     # the distance of any second string to an empty first string
   for j in range(1,n+1):
     for i in range(1,m+1):
       if string1[i-1] == string2[j-1]:  
         d[i][j] = d[i-1][j-1]      
       else:
         d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + 1 )

   return d[m][n]

#print(edit_distance("Sunday","Saturday"))

