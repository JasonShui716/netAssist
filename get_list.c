#include <stdio.h>
int main(){
	char type[10];
	char class[6];
	char fileName[50];
	int ret,count=0;
	for(int i=0;i<3;i++)
		scanf("%*s");
	while(1){
		ret = scanf("%s",type);
		if(ret==EOF)
			break;
		if(type[0]=='d')
			sprintf(class,"dir");
		else
			sprintf(class,"file");
		for(int i=0;i<7;i++){
			count++;
			scanf("%*s");
		}
		scanf("%s",fileName);
		printf("<p><a class=\"%s\" href=\"/%s/%s\">%s</a></p>\n",class,class,fileName,fileName);
	}
}
