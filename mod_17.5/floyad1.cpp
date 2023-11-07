#include<bits/stdc++.h>
using namespace std;
const int N = 1e3+7;
const int INF = 1e9+7;
int d[N][N];
int n,m;
void dist_initialization()
{
   for (int i=1; i<=n; i++)
   {
       for (int j=1; j<=n; j++)
       {
           if(i != j)
           {
            d[i][j]=INF;
           }
       }
   }
}

void print_matrix()
{
   for (int i=1; i<=n; i++)
   {
    for (int j=1; j<=n; j++)
    {
        if(d[i][j]==INF) cout<<"X"<<" ";
        else cout<<d[i][j]<<" ";
    }
    cout<<endl;
   }
}

int main(){
   cin>>n;
   dist_initialization();
   for (int i=1; i<=n; i++)
   {
    for (int j=1; j<=n; j++)
    {
      cin>>d[i][j];
    }
   }   

for (int k=1; k<=n; k++)
{
   for (int i=1; i<=n; i++)
   {
    for (int j=1; j<=n; j++)
    {
      d[i][j] = min (d[i][j] , d[i][k]+d[k][j]);
    }
   }
}

print_matrix();
   
  return 0;
}

// 4
// 0 5 9 100
// 100 0 2 8
// 100 100 0 7
// 4 100 100 0