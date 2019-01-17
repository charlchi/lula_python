import sys

d = {} # dictionary with {'team name' : score}

win = 3
tie = 1

for line in sys.stdin:
	line = line.rstrip('\r\n')
	team1, team2  = line.rsplit(', ', 1)
	name1, score1 = team1.rsplit(' ', 1)
	name2, score2 = team2.rsplit(' ', 1)
	if not name1 in d:
		d[name1] = 0
	if not name2 in d:
		d[name2] = 0
	if int(score1) == int(score2):
		d[name1] += tie
		d[name2] += tie
	elif int(score1) > int(score2):
		d[name1] += win
	else:
		d[name2] += win

# convert to tuple, sort by index 1 reverse, then index 0
scores = sorted(d.items(), key=lambda x: (-x[1], x[0]))

for i, v in enumerate(scores):
	print("%d. %s, %d pts" % (i + 1, v[0], v[1]))