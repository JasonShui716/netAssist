all:
	gcc -o auto_ftp ftp.c
	gcc -o getList getList.c
clean:
	rm getList
	rm auto_ftp
	rm -rf __pycache__
