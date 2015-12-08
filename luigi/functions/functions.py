def apache2_logrow(s):
		    row = [ ]
		    qe = qp = None # quote end character (qe) and quote parts (qp)
		    for s in s.replace('\r','').replace('\n','').split(' '):
		        if qp:
		            qp.append(s)
		        elif '' == s: # blanks
		            row.append('')
		        elif '"' == s[0]: # begin " quote "
		            qp = [ s ]
		            qe = '"'
		        elif '[' == s[0]: # begin [ quote ]
		            qp = [ s ]
		            qe = ']'
		        else:
		            row.append(s)
		        l = len(s)
		        if l and qe == s[-1]: # end quote
		            if l == 1 or s[-2] != '\\': # don't end on escaped quotes
		                row.append(' '.join(qp)[1:-1].replace('\\'+qe, qe))
		                qp = qe = None
		    return row


# def subconjunto(x,par):
# 		    x=df[x.dif_seg_clicks < par*60+1]
# 		    return x

