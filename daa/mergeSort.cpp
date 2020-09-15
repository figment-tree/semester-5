#include <iostream>
#include <chrono>
using namespace std::chrono;
using namespace std;

void merge(int* a, int l, int m, int r){
    int n = r - l + 1;
    int* result = new int[n];

    int i, j, k;
    i = l, j = m + 1, k = 0;

    while(i <= m && j <= r){
        if(a[i] < a[j]){
            result[k++] = a[i++];
        }
        else{
            result[k++] = a[j++];
        }
    }

    // If a couple of elements were left out in the left or right array
    // due to i > m or j > r, fill up the rest of the results array
    // with the remaining elements
    while(i <= m){
        result[k++] = a[i++];
    }
    while(j <= r){
        result[k++] = a[j++];
    }

    for(k = 0; k < n; k++){
        a[k + l] = result[k];
    }

    delete[] result;
}

void mergeSort(int* a, int l, int r){
    if(l >= r){
        return;
    }

    int mid = (l + r) / 2;
    mergeSort(a, l, mid);
    mergeSort(a, mid + 1, r);

    merge(a, l, mid, r);
}

int main() {
	int n;
	cout << "Enter array length:\n";
	cin >> n;

	int* a = new int[n];
	cout << "Enter elements:\n";

	for(int i = 0; i < n; i++){
	    cin >> a[i];
	}

	auto start = high_resolution_clock::now();
	mergeSort(a, 0, n - 1);
	auto stop = high_resolution_clock::now();

	cout << "Sorted array:\n";
	for(int i = 0; i < n; i++){
	    cout << a[i] << " ";
	}

	auto duration = duration_cast<microseconds>(stop - start);
	cout << "\nTime taken to sort: " << duration.count()  << " microseconds\n";

	delete[] a;

	return 0;
}
