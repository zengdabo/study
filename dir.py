#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, stat, time


class dirfileinfo:
    def __init__(self, name, width=0):
        self.width = width
        self.name = name
        statinfo = os.stat(name)
        self.time = time.strftime("%Y/%m/%d  %H:%M", time.localtime(statinfo.st_mtime))
        self.dir = "<DIR>" if stat.S_ISDIR(statinfo.st_mode) else "     "
        self.size = statinfo.st_size

    def __str__(self):
        return "{}{}{:{width}}{}".format(
            self.time, " " + self.dir, self.size, " " + self.name, width=self.width
        )

        # return '%s    %s    %s %s' % (self.time,self.dir,self.size,self.name)


if __name__ == "__main__":

    width = 0

    dir_list = []

    for name in os.listdir("."):
        item = dirfileinfo(name)
        width = max(width, len(str(item.size)))
        dir_list.append(name)

    for x in sorted(dir_list):

        print(dirfileinfo(x, width))

