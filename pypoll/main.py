import pandas as pd

# read a file
data_file = pd.read_csv("Resources/election_data.csv")

print(data_file)
         Voter ID   County Candidate
0        12864552    Marsh      Khan
1        17444633    Marsh    Correy
2        19330107    Marsh      Khan
3        19865775    Queen      Khan
4        11927875    Marsh      Khan
5        19014606    Marsh        Li
6        17775191    Queen    Correy
7        14003692    Marsh      Khan
8        14255761    Marsh      Khan
9        13870173    Marsh    Correy
10       16793141    Marsh      Khan
11       10591158    Bamoo    Correy
12       12344763  Trandee      Khan
13       18611011    Marsh      Khan
14       17845903    Marsh    Correy
15       12621425  Trandee      Khan
16       14365844    Marsh    Correy
17       13444989    Marsh    Correy
18       19204501  Trandee      Khan
19       10098063    Queen    Correy
20       19843246    Marsh    Correy
21       11509120    Marsh    Correy
22       13402499    Marsh    Correy
23       18138694    Marsh      Khan
24       15056703    Marsh      Khan
25       12026178    Queen      Khan
26       16667390    Marsh      Khan
27       12847422    Queen      Khan
28       10599242    Marsh      Khan
29       18558857    Queen    Correy
...           ...      ...       ...
3520971  17923362    Marsh      Khan
3520972  11357988    Marsh      Khan
3520973  13741548    Marsh    Correy
3520974  19929693    Marsh      Khan
3520975  16441960    Marsh      Khan
3520976  19992954    Marsh  O'Tooley
3520977  13845046    Marsh      Khan
3520978  18550834    Marsh    Correy
3520979  17540334    Queen      Khan
3520980  11020483    Queen  O'Tooley
3520981  15912885  Trandee      Khan
3520982  12609301    Marsh      Khan
3520983  14774584    Marsh        Li
3520984  13283796    Marsh      Khan
3520985  13359648    Bamoo      Khan
3520986  17391173    Queen    Correy
3520987  18995053    Queen      Khan
3520988  11867516    Bamoo        Li
3520989  18589143    Marsh      Khan
3520990  12282098    Marsh      Khan
3520991  16950418    Marsh    Correy
3520992  13715415    Marsh      Khan
3520993  18129849    Marsh      Khan
3520994  15785886    Marsh    Correy
3520995  12890090    Marsh    Correy
3520996  18050509    Marsh      Khan
3520997  13060332    Marsh      Khan
3520998  16754708    Queen      Khan
3520999  12083146    Queen      Khan
3521000  14526187    Queen  O'Tooley

[3521001 rows x 3 columns]
In [17]:
# calculate the total number of votes
total_votes = len(data_file)
total_votes
Out[17]:
3521001
In [18]:
# list of candidates who received votes
candidates_count = data_file["Candidate"].value_counts()
candidates_count
Out[18]:
Khan        2218231
Correy       704200
Li           492940
O'Tooley     105630
Name: Candidate, dtype: int64
In [19]:
# percentage of votes each candidate won
percentage_votes = (candidates_count/total_votes)*100
percentage_votes
Out[19]:
Khan        63.000011
Correy      19.999994
Li          13.999996
O'Tooley     2.999999
Name: Candidate, dtype: float64
In [20]:
# announce the winner
winner = candidates_count.idxmax()
winner
Out[20]:
'Khan'
In [21]:
# print the results
print("Election results")

print("--------------------------------------------------------------------------")

print("Total votes: " + str(total_votes))

print("----------------------------------------------------------------------------")

print("Khan:" + " " + str(round(percentage_votes[0],3)) + "%" + "("+str(candidates_count[0])+")")
      
print("Correy:" + " " + str(round(percentage_votes[1],3)) + "%" + "("+str(candidates_count[1])+")")
      
print("Li:" + " " + str(round(percentage_votes[2],3)) + "%" + "("+str(candidates_count[2])+")")
      
print("O'Tooley:" + " " + str(round(percentage_votes[3],3)) + "%" + "("+str(candidates_count[3])+")")

print("----------------------------------------------------------------------------------------")
      
print("winner: " + winner)
Election results
--------------------------------------------------------------------------
Total votes: 3521001
----------------------------------------------------------------------------
Khan: 63.0%(2218231)
Correy: 20.0%(704200)
Li: 14.0%(492940)
O'Tooley: 3.0%(105630)
----------------------------------------------------------------------------------------
winner: Khan
In [22]:
# convert the output into a text file
file = open('pypoll.txt','w')
file.write("Election results")
file.write("\n....................................................................................")
file.write("\nTotal votes: " + str(total_votes))
file.write("\n----------------------------------------------------------------------------")
file.write("\nKhan:" + " " + str(round(percentage_votes[0],3)) + "%" + "("+str(candidates_count[0])+")")
file.write("\nCorrey:" + " " + str(round(percentage_votes[1],3)) + "%" + "("+str(candidates_count[1])+")")
file.write("\nLi:" + " " + str(round(percentage_votes[2],3)) + "%" + "("+str(candidates_count[2])+")")
file.write("\nO'Tooley:" + " " + str(round(percentage_votes[3],3)) + "%" + "("+str(candidates_count[3])+")")
file.write("\n----------------------------------------------------------------------------------------")
file.write("\nwinner: " + winner)
file.close()
