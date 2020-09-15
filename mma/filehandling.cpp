#include <iostream>
#include <fstream>

using namespace std;

// Writing into a .txt file
void writeTo(string fileName){
  ofstream fout;

  try{
    fout.open(fileName, ios::out | ios::app);

    string input;
    string line;

    cout << "Enter contents that need to be added to file:\n\n";

    while(getline(cin, line))
    {
        if (line == "-1") // to indicate that this is the end of the input
            break;

        input += line + '\n';
    }

    fout << input;

    cout << "\nFinished writing to file.\n\n";
    fout.close();
  }

  catch(const ofstream::failure& e) {
    cout << "Exception opening/writing to file";
  }

}

// Reading from a .txt file
void readFrom(string fileName){
  ifstream fin;

  try {
    fin.open(fileName, ios::in);

    string output;

    while(getline(fin, output))
    {
      cout << output << "\n";
    }

    cout << "\nFinished reading from file.\n";

    fin.close();
  }

  catch (const ifstream::failure& e) {
    cout << "Exception opening/reading file";
  }
}

int main(){

  string fileName;
  cout << "Enter file name: ";
  cin >> fileName;

  writeTo(fileName);
  readFrom(fileName);

  return 0;
}
