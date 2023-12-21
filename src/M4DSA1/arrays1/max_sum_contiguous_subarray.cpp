#include<iostream>
#include<vector>
#include<climits>

using namespace std;

// Time Complexity: O(n) | Space Complexity: O(1)
// Note: kadane's algorithm

class Solution{
    public:
    int max_sum(const vector<int> & arr) {
        int max_sum = INT_MIN, sum = 0;

        for(int num: arr){
            sum += num;
            max_sum = max(sum, max_sum);
            if (sum < 0) sum = 0;
        }

        return max_sum;
    }
};



int main(){
    Solution solution;
    cout << solution.max_sum({-2, 1, -3, 4, -1, 2, 1, -5, 4}) << endl;
}