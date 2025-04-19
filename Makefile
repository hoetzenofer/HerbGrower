IP=192.168.178.63
USER=hoetzenofer

send:
	scp -r ../HerbGrower $(USER)@$(IP):/home/$(USER)
