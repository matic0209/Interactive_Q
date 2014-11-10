.PHONY: clean

CC=g++
CFLAGS= -c -g3 -g  -Wall -fopenmp -Wno-deprecated
LDFLAGS= -fopenmp -g3 -g
OBJS = main.o

query : $(OBJS)
		$(CC) $(LDFLAGS) -o3 -o  $@ $^

$(OBJS): %.o: %.cpp
		$(CC) $(CFLAGS) $<



clean:
		rm -rf *.o query
