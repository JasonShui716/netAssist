all:
	gcc -o ftp_ls ftp_ls.c
	gcc -o get_list get_list.c
clean:
	rm get_list
	rm ftp_ls
	rm -rf __pycache__
