#include<bits/stdc++.h>
using namespace std;
const int N = 1e5+7;
typedef pair<int,int>pii;
int dist[N];
vector<pii>g[N];
int n,m;
const int INF = 30000;
void ford_bellman(int s)
{
   for (int i=1; i<=n; i++)
   {
       dist[i]=INF;
   }

   dist[s]=0;

   int t=n;
   while (t--)
   {
     for (int i=1; i<=n; i++)
     {
         for(pii upair  : g[i])
         {
            int v = upair.first;
            int w = upair.second;

            if(dist[i] !=INF && dist[v] > dist[i] + w)
            {
                dist[v] = dist[i]+w;
            }
         }
     }
   }
   
}

int main(){
   cin>>n>>m;
   while (m--)
   {
     int u,v,w;
     cin>>u>>v>>w;
     g[u].push_back({v,w});
   }

   ford_bellman(1);
   
   for (int i=1; i<=n; i++)
   {
       cout<<dist[i]<<" ";
   } 

    return 0;
}
// 4 5
// 1 2 10
// 2 3 10
// 1 3 100
// 3 1 -10
// 2 3 1