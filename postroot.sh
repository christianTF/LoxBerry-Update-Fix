#!/bin/bash
# Will be executed as user "root".
cp -v -f $LBPDATA/$3/loxberryupdatecheck.pl $LBHOMEDIR/sbin/
chown root:root $LBHOMEDIR/sbin/loxberryupdatecheck.pl
exit 0
