publish:
	git config --global user.email josetechteam@gmail.com
	git config --global user.name josetechteam
	git config --global push.default simple
	git add .
	git commit -m "automatic git update from Makefile"
	git push
