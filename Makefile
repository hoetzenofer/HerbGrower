IP=192.168.178.63
USER=hoetzenofer
DIR_SRC=.
DIR_DST=HerbGrower

send:
	scp -r $(DIR_SRC) $(USER)@$(IP):/home/$(USER)/$(DIR_DST)

