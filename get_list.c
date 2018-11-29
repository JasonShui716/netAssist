#include <stdio.h>
int main(){
	char type[10];
	char fileName[50];
	int ret,count=0;
	for(int i=0;i<3;i++)
		scanf("%*s");
	while(1){
		ret = scanf("%s",type);
		if(ret==EOF|count>1000)
			break;
		if(type[0]=='d')
			printf("<p style=\"color:green;\">");
		else
			printf("<p style=\"color:blue;\">");
		for(int i=0;i<7;i++){
			count++;
			scanf("%*s");
		}
		scanf("%s",fileName);
		printf("%s\n</p>",fileName);
	}
}
