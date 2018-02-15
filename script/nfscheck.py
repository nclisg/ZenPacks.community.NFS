#!/usr/bin/env python

NFSD = '/proc/net/rpc/nfsd'

def main():
    data = open(NFSD)

    elements = []

    for line in data:
        if line.startswith('proc3'):
            elements = tuple(line.split()[2:])

    print("OK | null=%s, getattr=%s, setattr=%s, lookup=%s, access=%s, readlink=%s, read=%s, write=%s, create=%s, mkdir=%s, symlink=%s, mknod=%s, remove=%s,rmdir=%s, rename=%s, link=%s, readdir=%s, readdirplus=%s, fsstat=%s, fsinfo=%s, pathconf=%s, commit=%s" %
          elements)


if __name__ == "__main__":
    main()
