IP := 192.168.178.63
USER := hoetzenofer
DIR_SRC := .
DIR_DST := HerbGrower
EXCL := .git/

send:
	rsync -av --exclude=$(EXCL) $(DIR_SRC)/ $(USER)@$(IP):$(DIR_DST)

