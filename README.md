get_win8key
===========

script to read a preinstalled Windows 8.x OEM license key from a PC's firmware

Description
-------------
PCs with a preinstalled Windows 8.x OEM version don't seem to ship with any printed license record, CD Key, etc.
Instead it looks like that the PC's individual license has been saved in the device's firmware (ACPI). When the user tries to reinstall Windows, the Windows Setup reads the license key from the firmware memory, so there's no need to manually type in the actual Windows key.

To still be able to backup / inventorize the license key, this script tries to read the Windows 8.x key from the PC firmware.
(from ACPI -> MSDM table -> byte offset 56 to end)


Windows Usage
-------------

run "get_win8key.exe" or "python get_win8key.py" from a Windows shell.

Linux Usage
-----------

sudo python get_win8key.py

Requirements
-------------

Executable:
* Windows Vista or higher (32 or 64 bit)

Python:
* Linux or Windows
* Python 2.7 or 3.4

Files
-------------
get_win8key.py..................the script
get_win8key.exe.................compiled with py2exe
