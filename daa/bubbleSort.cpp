#include <iostream>
#include <chrono>
using namespace std::chrono;
using namespace std;

void bubbleSort(int* a, int n){
  if(n <= 1){
    return;
  }

  bool isSorted;

  for(int i = 0; i < n; i++){
    isSorted = true;
    for(int j = 0; j < n - i - 1; j++){
      if(a[j] > a[j + 1]){
        isSorted = false;

        int t = a[j];
        a[j] = a[j + 1];
        a[j + 1] = t;
      }
    }
    if(isSorted){
      break;
    }
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
	bubbleSort(a, n);
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
