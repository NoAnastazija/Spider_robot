#include <iostream>
#include <cstdio>
#include <cstring>
#include <conio.h>

using namespace std;

int main()
{
     Serial* port = new Serial("COM3");
    if (port->IsConnected()) cout << "Connected!" << endl;

    char data[4] = "";
    char command[1]="";
    int datalength = 4;  
    int readResult = 0;
    int n;

    cout<<"Enter your command: " <<endl;

while(1)
{
    if (_kbhit()) //determines if a key has been pressed or not
    {
        cin.get(command, 1);     //input command 
        int msglen = strlen(command);
        if (port->WriteData(command, msglen));   //write to arduino
        printf("\n(writing success)\n");
        cout << "Enter your command: ";
    }

    //read from arduino output
    n = port->ReadData(data, 4);
    if (n != -1)
    {
        data[n] = 0;
        cout <<"arduino: " data << endl;
    }
    Sleep(10);
}
  

/*void thread1()
{
    while (1)
    {
        std::cout << "Enter your command: ";
        std::cin.get(command, 2);     //input command 
        int msglen = strlen(command);
        if (port->WriteData(command, msglen));   //write to arduino
        printf("\n(writing success)\n");
    }
}

void thread2()
{
    while (1)
    {
        int n = port->ReadData(data, 4);
        if (n != -1){
            data[n] = 0;
            cout <<"arduino: " data << endl;
        }
        Sleep(10);
    }
}
*/

  /*  cin.get(command, 2);
    cin.clear();
    cin.ignore(INT_MAX,'\n');
    int msglen=strlen(command);/
    sleep(10);
*/

    system("pause");
    return 0;
}