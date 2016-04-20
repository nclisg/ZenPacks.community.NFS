#!/usr/bin/env python

NFSD = '/proc/net/rpc/nfsd'

def main():
    data = open(NFSD)

    elements = []

    for line in data:
        if line.startswith('proc3'):
            elements = line.split()

    print "OK | getattr=%s, setattr=%s, lookup=%s, access=%s, readlink=%s, read=%s, write=%s, create=%s, mkdir=%s, symlink=%s, mknod=%s, remove=%s,rmdir=%s, rename=%s, link=%s, readdir=%s, readdirplus=%s, fsstat=%s, fsinfo=%s, pathconf=%s, commit=%s" % (elements[2], elements[3], elements[4], elements[5], elements[6], elements[7], elements[8], elements[9], elements[10], elements[11], elements[12], elements[13], elements[14], elements[15], elements[16], elements[17], elements[18], elements[19], elements[20], elements[21], elements[22])


if __name__ == "__main__":
    main()
