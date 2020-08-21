#include <iostream>
#include <chrono>
using namespace std::chrono;
using namespace std;

void selectionSort(int* a, int n){
  if(n <= 1){
    return;
  }

  int minIndex;

  for(int i = 0; i < n; i++){
    minIndex = i;
    for(int j = i; j < n; j++){
      if(a[j] < a[minIndex]){
        minIndex = j;
      }
    }
    int t = a[i];
    a[i] = a[minIndex];
    a[minIndex] = t;
  }
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
	selectionSort(a, n);
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
