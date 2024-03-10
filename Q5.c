#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverte(char* str)
{
    int tam = strlen(str);
    char* inicio = str;
    char* fim = str + tam - 1;
    while (inicio<fim)
    {
        char temp = *inicio;
        *inicio = *fim;
        *fim = temp;
        inicio ++;
        fim--;
    }
    
}

int main(int argc, char const *argv[])
{
    char str[21] = "string para reverter";
    reverte(str);
    printf("%s\n", str);
    system("pause");
    return 0;
}
