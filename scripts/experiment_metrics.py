"""Descriptive independent conversion comparison; no automatic causal conclusion."""
import argparse, json, math
def wilson(successes,total,z=1.96):
    if isinstance(total,bool) or isinstance(successes,bool) or not isinstance(total,int) or not isinstance(successes,int) or total<=0 or not 0<=successes<=total:
        raise ValueError('Need integer counts, 0 <= successes <= total, total > 0')
    p=successes/total;d=1+z*z/total
    center=(p+z*z/(2*total))/d
    half=z*math.sqrt(p*(1-p)/total+z*z/(4*total*total))/d
    return max(0,center-half),min(1,center+half)
def compare(a,na,b,nb):
    alo,ahi=wilson(a,na);blo,bhi=wilson(b,nb)
    difference=b/nb-a/na
    # Newcombe score interval for independent proportions.
    low=difference-math.sqrt((b/nb-blo)**2+(ahi-a/na)**2)
    high=difference+math.sqrt((bhi-b/nb)**2+(a/na-alo)**2)
    return {'a_rate':a/na,'b_rate':b/nb,'difference':difference,'difference_95_interval':[low,high],
            'interpretation':'探索结果；需要检查随机化、预设指标、样本与护栏，不能仅由此证明因果或保证收益。'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('a',type=int);p.add_argument('na',type=int);p.add_argument('b',type=int);p.add_argument('nb',type=int);x=p.parse_args()
    print(json.dumps(compare(x.a,x.na,x.b,x.nb),ensure_ascii=False,indent=2))
