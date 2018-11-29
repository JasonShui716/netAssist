#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
    FILE *fp;
    char str[255];
    if (argc != 4)
    {
        printf("%s\n%s\n",
               "Usage:",
               " auto_ftp <ip> <user> <pass> <filename>");
        exit(1);
    }
    if ((fp = popen("ftp -n", "w")) == NULL)
    {
        puts("Run ftp fail !");
        exit(2);
    }
    //while ((fgets(str,255,fp))!=NULL) puts(str);
    fprintf(fp, "open %s\n", argv[1]);
    fprintf(fp, "user %s %s\n", argv[2], argv[3]);
    fprintf(fp, "binary\n");
    fprintf(fp, "prompt\n");
    fprintf(fp, "ls\n");
    //fprintf(fp, "mget *%s\n", argv[4]);
    fprintf(fp, "bye\n");
    pclose(fp);
}
