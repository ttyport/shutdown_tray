#!/bin/bash

if [ `whoami` != 'root' ]
  then
    echo "error: you cannot perform this operation unless you are root."
    exit
fi

pip3 install -r requirements.txt

echo "#!/bin/bash
python3 /usr/share/shutdown_tray/tray.py" > /usr/bin/shutdown_tray

mkdir /usr/share/shutdown_tray/
cp icon.png /usr/share/shutdown_tray/
cp tray.py /usr/share/shutdown_tray/

chmod +x /usr/bin/shutdown_tray
