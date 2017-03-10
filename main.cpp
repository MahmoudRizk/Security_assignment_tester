#include <iostream>
#include <string>

using namespace std;

int main(int argc, char*argv[]){

  string p =argv[1]; //from python script
  string q =argv[2]; //from python script.
	string e =argv[3]; //from python script.

	int x = stoi(p);
	int y = stoi(q);

  cout << x + y << endl; 

  return 0;
}
