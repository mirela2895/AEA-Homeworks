/*********************************************
 * OPL 12.8.0.0 Model
 * Author: mchitaniuc
 * Creation Date: Oct 18, 2018 at 4:25:38 PM
 *********************************************/
using CP;

int n=10;
int d=10;
range letters=1..n;
int k=n; // words
range words=1..k;

dvar int x[words][letters] in 0..3; // ACGT

subject to
{
forall(ordered i,j in words) d<=sum(k in letters) (x[i][k]!=x[j][k]);

forall(i in words) 
    count(all(j in letters)x[i][j],1)+
    count(all(j in letters)x[i][j],2)>=n/2;

forall(ordered i,j in words) d<=sum(k in letters) (x[i][k]!=(3-x[j][k]));
}

execute
{

function letterDisplay(n)
{
if (n==0) return "A";
if (n==1) return "C";
if (n==2) return "G";
if (n==3) return "T";
fail();

}


for(var w in words)
{
for(var l in letters) write(letterDisplay(x[w][l]));
writeln();
}

}