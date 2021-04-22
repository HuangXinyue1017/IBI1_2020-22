import io

dict = {'AA':4,
		'RA':-1,'RR':5,
		'NA':-2,'NR':0, 'NN':6,
		'DA':-2,'DR':-2,'DN':1, 'DD':6,
		'CA':0, 'CR':-3,'CN':-3,'CD':-3,'CC':9,
		'QA':-1,'QR':1, 'QN':0, 'QD':0, 'QC':-3,'QQ':5,
		'EA':-1,'ER':0, 'EN':0, 'ED':2, 'EC':-4,'EQ':2, 'EE':5,
		'GA':0 ,'GR':-2,'GN':0, 'GD':-1,'GC':-3,'GQ':-2,'GE':-2,'GG':6,
		'HA':-2,'HR':0, 'HN':1, 'HD':-1,'HC':-3,'HQ':0, 'HE':0, 'HG':-2,'HH':8,
		'IA':-1,'IR':-3,'IN':-3,'ID':-3,'IC':-1,'IQ':-3,'IE':-3,'IG':-4,'IH':-3,'II':4,
		'LA':-1,'LR':-2,'LN':-3,'LD':-4,'LC':-1,'LQ':-2,'LE':-3,'LG':-4,'LH':-3,'LI':2, 'LL':4,
		'KA':-1,'KR':2, 'KN':0, 'KD':-1,'KC':-3,'KQ':1, 'KE':1, 'KG':-2,'KH':-1,'KI':-3,'KL':-2,'KK':5,
		'MA':-1,'MR':-1,'MN':-2,'MD':-3,'MC':-1,'MQ':0, 'ME':-2,'MG':-3,'MH':-2,'MI':1, 'ML':2, 'MK':-1,'MM':5,
		'FA':-2,'FR':-3,'FN':-3,'FD':-3,'FC':-2,'FQ':-3,'FE':-3,'FG':-3,'FH':-1,'FI':0, 'FL':0, 'FK':-3,'FM':0, 'FF':6,
		'PA':-1,'PR':-2,'PN':-2,'PD':-1,'PC':-3,'PQ':-1,'PE':-1,'PG':-2,'PH':-2,'PI':-3,'PL':-3,'PK':-1,'PM':-2,'PF':-4,'PP':7,
		'SA':1, 'SR':-1,'SN':1, 'SD':0, 'SC':-1,'SQ':0, 'SE':0, 'SG':0, 'SH':-1,'SI':-2,'SL':-2,'SK':0, 'SM':-1,'SF':-2,'SP':-1,'SS':4,
		'TA':0, 'TR':-1,'TN':0, 'TD':-1,'TC':-1,'TQ':-1,'TE':-1,'TG':-2,'TH':-2,'TI':-1,'TL':-1,'TK':-1,'TM':-1,'TF':-2,'TP':-1,'TS':1, 'TT':5,
		'WA':-3,'WR':-3,'WN':-4,'WD':-4,'WC':-2,'WQ':-2,'WE':-3,'WG':-2,'WH':-2,'WI':-3,'WL':-2,'WK':-3,'WM':-1,'WF':1, 'WP':-4,'WS':-3,'WT':-2,'WW':11,
		'YA':-2,'YR':-2,'YN':-2,'YD':-3,'YC':-2,'YQ':-1,'YE':-2,'YG':-3,'YH':2, 'YI':-1,'YL':-1,'YK':-2,'YM':-1,'YF':3, 'YP':-3,'YS':-2,'YT':-2,'YW':2, 'YY':7,
		'VA':0, 'VR':-3,'VN':-3,'VD':-3,'VC':-1,'VQ':-2,'VE':-2,'VG':-3,'VH':-3,'VI':3, 'VL':1, 'VK':-2,'VM':1, 'VF':-1,'VP':-2,'VS':-2,'VT':0, 'VW':-3,'VY':-1,'VV':4}

# get sequence
def extract(lines):
	s = ''
	for line in lines:
		if(line[0] != '>'):
			s += line.strip()
	return s

with open('SOD2_human.fa','r') as f:
	s1 = extract(f.readlines())

with open('SOD2_mouse.fa','r') as f:
	s2 = extract(f.readlines())

with open('RandomSeq.fa','r') as f:
	s3 = extract(f.readlines())

def alignment(seq1,seq2):
	distance = 0
	score = 0
	tot = len(seq1)
	for i in range(0,tot):
		if (seq1[i] != seq2[i]):
			distance += 1
		pair = seq1[i] + seq2[i]
		if (pair not in dict):
			pair = seq2[i] + seq1[i]
		score += dict[pair]
	print('distance:%d' % distance)
	print('similarity: %.2lf' % ((1-distance/tot)*100),end='%\n')
	print('score:%d\n' % score)

print('human gene:%s\n' % s1)
print('mouse gene:%s\n' % s2)
alignment(s1,s2)

print('human gene:%s\n' % s1)
print('random gene:%s\n' % s3)
alignment(s1,s3)

print('mouse gene:%s\n' % s2)
print('random gene:%s\n' % s3)
alignment(s2,s3)
