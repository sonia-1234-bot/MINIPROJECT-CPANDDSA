#include <iostream>
#include<string.h>


using namespace std;

void encode(string str,int n)
{
    int dup;
    string str1;
    string k;
    cout<<"The encoded message is ";
    for(int i=0;i<str.length();i++)
    {
        int l;
        dup=int(str[i]);
        l=dup+n;
        if(l>122)
        {
         l=l-122;
         l=97+l-1;
        }  
        k=char(l);
        cout<<k;
        
    }
    
}

void decode(string str,int n)
{
    int dup;
    string str1;
    string k;
    cout<<"The decoded message is ";
    for(int i=0;i<str.length();i++)
    {
        dup=int(str[i]);
        int l=dup-n;
        if(l<97)
        {
            l=97-l;
            l=123-l;
        }
        k=char(l);
        cout<<k;
        
    }
}

int main()
{
    string s,str;
    int n;
    cout<<"Type encode to encrypt and decode to decrypt: ";
    cin>>s;
    cout<<"Type the message: ";
    cin>>str;
    cout<<"Enter the number of shifts: ";
    cin>>n;
    if(s=="encode")
    {
        encode(str,n);
    }
    else if(s=="decode")
    {
        decode(str,n);
    }
    else
    {
        cout<<"Invalid input!!!\n";
    }
    return 0;
}
