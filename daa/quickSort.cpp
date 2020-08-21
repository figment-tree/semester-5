#include <iostream>
#include <chrono>
using namespace std::chrono;
using namespace std;

int partition(int* a, int l, int r){
    int p = l;

    //find pivot i.e. find the position at which the element currently at
    // a[l] needs to be in the sorted array by counting the number of elements
    // in the array that are smaller than or equal to it
    for(int i = l + 1; i <= r; i++){
        if(a[i] <= a[l]){
            p++;
        }
    }

    //move a[l] to pivot
    int t = a[l];
    a[l] = a[p];
    a[p] = t;

    //partition
    for(int i = l, j = r; i < p && j > p; i++, j--){
        while(a[i] <= a[p] && i < p){
            i++;
        }
        while(a[j] > a[p] && j > p){
            j--;
        }
        if(i < p && j > p){
            int t = a[i];
            a[i] = a[j];
            a[j] = t;
        }
    }

    return p;
}

void quickSort(int* a, int l, int r) {
    if(l >= r){
        return;
    }

    int pivot = partition(a, l, r);

    quickSort(a, l, pivot - 1);
    quickSort(a, pivot + 1, r);
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
	quickSort(a, 0, n - 1);
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
