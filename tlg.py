t = int(input())
lead_diff = [0]*t
leader_r = [0]*t
p1_score = 0
p2_score = 0
for i in range(t):
    p1, p2 = [int(y) for y in input().split()]
    p1_score += p1
    p2_score += p2
    temp_diff = p1_score - p2_score
    lead_diff[i] = abs(temp_diff)
    if (temp_diff > 0):
        leader_r[i] = 1
    else:
        leader_r[i] = 2

print str(leader_r[lead_diff.index(max(lead_diff))]) + " " + str(max(lead_diff))
