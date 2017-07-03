#include <stdio.h>
#include <stdint.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>
#include <fcntl.h>

#define PROM_ADDR 0x1FC00000
#define PROM_LEN (512 * 1024)

int main(int argc, const char **argv) {
	uint8_t *addr;
	int fd;
	ssize_t sz;
	if ((fd = open("/dev/mem", O_RDONLY | O_SYNC)) < 0 ) {
		printf("Error opening file. \n");
		close(fd);
		return -1;
	}
	addr = (uint8_t *)mmap(0, PROM_LEN, PROT_READ, MAP_SHARED,
				fd, PROM_ADDR);
	if (addr == (void*)-1) {
		perror("mmap");
		return -1;
	}
	sz = write(STDOUT_FILENO, addr, PROM_LEN);
	assert(sz == PROM_LEN);

	return 0;
}
