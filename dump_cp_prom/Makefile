CFLAGS = -Os -g

all: dump_cp_prom

.PHONY: clean

dump_cp_prom: dump_cp_prom.c
	mipsel-linux-gcc -o $@ $< $(CFLAGS)

clean:
	rm -f dump_cp_prom
