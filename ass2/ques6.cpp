#include<bits/stdc++.h>

using namespace std;



string get_complement(string s)
{
	for(int i = 0; i<s.size() ; i++)
	{
		if(s[i] == 'A')
			s[i] = 'U';
		else if(s[i] == 'U')
			s[i] = 'A';
		else if(s[i] == 'G')
			s[i] = 'C';
		else if(s[i] == 'C')
			s[i] = 'G' ;
	}
	reverse(s.begin() ,  s.end());
	return s;
}


int main(int argc, char const *argv[])
{
	string s1;
	cout << "Please enter the string for which you want conservations across the complement" << endl;
	cin >> s1;

	string s2 = get_complement(s1);

	// we have to now tmake a dotplot
	char arr[100][100];

	for(int i = 0 ; i<s2.size() ; i++)
	{
		for (int j = 0 ; j<s1.size()  ; ++j)
		{
			arr[i][j] = '_';
		}
	}

	for(int i = 1 ; i<= s1.size() ; i++)
		arr[0][i] = s1[i-1];

	for(int i = 1 ; i<= s2.size() ; i++)
		arr[i][0] = s2[i-1];




	for (int i = 1 ; i<=s2.size() ; i++)
	{
		for(int j = 1 ; j<=s1.size(); j++)
		{
			if (s1[j-1] == s2[i-1])
				arr[i][j] = 'X';
		}
	}


	// now we print the array

	for(int i = 0 ; i<s2.size() ; i++)
	{
		for(int j = 0 ; j<s1.size() ; j++)
		{
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;

	return 0;
}