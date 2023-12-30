#include<iostream>
#include<vector>

using namespace std;

class Solution {
    public:
    int equilibrium_index(vector<int>& A){     
        vector<int> prefix_sum(A.size()+1, 0);

        for(int i=0; i<A.size(); i++) 
            prefix_sum[i+1] = prefix_sum[i] + A[i];

        for(int i=1; i<prefix_sum.size(); i++) 
            if(prefix_sum[i-1] == (prefix_sum[prefix_sum.size()-1] - prefix_sum[i])) return i-1;

        return -1;
    }
};

int main() {
    Solution solution;
    vector<int> input = {-7, 1, 5, 2, -4, 3, 0};

    int index = solution.equilibrium_index(input);
    cout << "equilibrium index: " << index;
}