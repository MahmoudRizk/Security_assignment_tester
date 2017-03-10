#include <iostream>
#include <string>

using namespace std;

int main(int argc, char*argv[]){

  string q =argv[2]; //from python script.
  string p =argv[1]; //from python script
	string e =argv[3]; //from python script.

	int x = stoi(p);
	int y = stoi(q);
	int z = stoi(e);

  	int result = x + y ;
    cout << to_string(result) << endl; //print in string format.

  return 0;
}
