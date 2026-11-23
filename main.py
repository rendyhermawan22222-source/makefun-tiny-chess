import json as j,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
V=0,100,320,330,500,900,0
Y=lambda x:x-6*(x>6)
N=14,18,31,33,-14,-18,-31,-33
D=15,17,-15,-17
W=1,16,-1,-16
G=D+W
P="OOOOTYYTTTYTOYcYT^c^YchccmmhOOOO!'11';OO1OY^1T^c1O^c1TY^';OT!'11;EEEEOOOEOTYETTYEOYYETTYEOOO;EEEcmYOccOOE;;;;11'1''!1''!1''!1''!"
Z={0:13,7:14,4:12,112:7,119:11,116:3}
b=[0]*128
s=c=0;e=-1;k=[4,116]
n=S=0;L=1e5
T={}
def C(x,q):
 t=Y(x);h=min(q&7,7-(q&7));z=int("012003"[t-1])*32+(q>>4 if x<7 else 7-(q>>4))*4+h;v=V[t]+ord(P[z])-79
 return v-v*2*(x>6)
def H(p,y):return j.load(u.urlopen(U+p,j.dumps(y).encode()))
def F(f):
 global s,c,e,S,b
 q=f.split();b=[0]*128;S=0;v=112
 for h in q[0]:
  if h=="/":v-=24
  elif h.isdigit():v+=int(h)
  else:
   y='PNBRQKpnbrqk'.index(h)+1;b[v]=y;S+=C(y,v)
   if y%6==0:k[y>6]=v
   v+=1
 s=q[1]=="b";c=sum(1<<i for i in range(4)if"KQkq"[i]in q[2])
 e=ord(q[3][0])+16*ord(q[3][1])-881 if q[3]!="-" else-1
def A(q,w):
 u=2*w-1;z=3-3*u
 for t in(q-15*u,q-17*u):
  if not t&136 and b[t]==1+z:return 1
 for o in N+G:
  t=q+o
  if not t&136 and b[t]-z==2+4*(o in G):return 1
 for o in G:
  t=q+o
  while not t&136:
   x=b[t]
   if x-z in(5,4-(o in D)):return 1
   if x:break
   t+=o
 return 0
def M(o=0):
 m=[];w=s==0
 for q,x in enumerate(b):
  if not x or(x<7)!=w:continue
  t=Y(x)
  if t==1:
   d=32*w-16;z=q+d
   if not o and b[z]==0:
    m.append(q|(z<<7)|(z>>4==7*w)*5<<14)
    if q>>4==6-5*w and b[q+2*d]==0:m.append(q|(q+2*d)<<7)
   for v in(q+d-1,q+d+1):
    if not v&136 and(y:=b[v])and(y<7)!=w:m.append(q|(v<<7)|(v>>4==7*w)*5<<14)
    elif 0<=v==e:m.append(q|(v<<7))
  else:
   ds=(N,D,W,G,G)[t-2];sl=2<t<6
   for d in ds:
    v=q+d
    while not v&136:
     if(y:=b[v]):
      if(y<7)!=w:m.append(q|(v<<7))
      break
     if not o:m.append(q|(v<<7))
     if not sl:break
     v+=d
 if not o:
  for dd in(1,-1):
   ks=4+112*s;r=(dd<0)+1<<2*s;ke=ks+2*dd
   if c&r and b[ks+dd]==b[ke]==0 and not(dd<0 and b[ks+3*dd])and not sum(A(x,s==1)for x in(ks,ks+dd,ke)):m.append(ks|(ke<<7))
 return m
def K(m):
 global c,e,S
 f=m&127;v=(m>>7)&127;r=(m>>14)&7;x=b[f];t=Y(x);y=b[v];w=v;nx=r+6*s if r else x
 if t==1 and v==e and y==0:w=v-16+32*s;y=b[w];b[w]=0
 oS=S;S+=C(nx,v)-C(x,f)-(C(y,w)if y else 0);b[v]=nx;b[f]=0;o=-1
 if t==6 and abs(v-f)==2:
  o=(v+1,v-1)if v>f else(v-2,v+1);p=b[o[0]];S+=C(p,o[1])-C(p,o[0]);b[o[1]],b[o[0]]=p,0
 if t==6:k[s]=v
 z=(m,y,w,c,e,o,oS);c&=Z.get(f,15)&Z.get(v,15);e=v-16+32*s if t==1 and abs(v-f)==32 else-1
 return z
def B(z):
 global c,e,S
 m,y,w,a,d,o,S=z;f=m&127;v=(m>>7)&127;r=(m>>14)&7;x=b[v]
 if o!=-1:b[o[0]],b[o[1]]=b[o[1]],0
 b[f]=1+6*s if r else x;b[v]=0
 if y:b[w]=y
 if Y(x)==6:k[s]=f
 c,e=a,d
def O(ms):
 return sorted(ms,key=lambda m:16*V[Y(b[(m>>7)&127])]-V[Y(b[m&127])]+9000*(m>>14),reverse=1)
def r(a,be,d,p):
 global n,s
 n+=1
 if n>L:1/0
 q=d<=0
 ic=A(k[s],s==1)
 if q:
  t=S*(1-2*s)
  if t>=be:return be
  if t>a:a=t
 else:
  ky=(bytes(b),s,c,e);a0=a
  if(y:=T.get(ky)):
   v=y[2]-p*(y[2]>90000)+p*(y[2]<-90000)
   if y[0]>=d and(v>=be or y[1]==0):return v
 ms=O(M(0 if ic else 1)if q else M())
 bs=-100000
 for m in ms:
  h=K(m);s=1-s
  if A(k[1-s],s==0):s=1-s;B(h);continue
  x=-r(-be,-a,0 if q else d-1,p+1)
  s=1-s;B(h)
  if x>bs:bs=x
  if x>a:a=x
  if a>=be:break
 if bs==-100000:return a if q and not ic else p-100000 if ic else 0
 if not q and bs>a0:T[ky]=(d,bs>=be,bs+p*(bs>90000)-p*(bs<-90000))
 return bs if not q else a
def rt(g):
 global n,s,T
 n=0
 T={}
 F(g["fen"]);ms=M();lg=[]
 for m in ms:
  h=K(m);s=1-s
  if not A(k[1-s],s==0):lg.append(m)
  s=1-s;B(h)
 bm=lg[0]
 for d in range(16):
  try:
   a=-1e5;be=1e5
   for m in lg:
    h=K(m);s=1-s;x=-r(-be,-a,d,1)
    s=1-s;B(h)
    if x>a:a=x;bm=m
   lg.remove(bm);lg.insert(0,bm)
  except:break
 return bm
Q=lambda q:chr(97+(q&7))+chr(49+(q>>4))
while 1:
 try:g=H("/game",{})
 except:continue
 if g["status"]=="done":break
 while g["status"]=="your_move":
  try:
   m=rt(g);mv=Q(m&127)+Q(m>>7&127)+"q"*(m>>14>0)
   assert mv in g["legal_moves"]
  except:mv=g["legal_moves"][0]
  try:g=H("/move",{"game":g["game"],"move":mv})
  except:g=H("/game",{})
