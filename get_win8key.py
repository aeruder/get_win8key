import sys
import acpi

#####################################################
#script to query windows 8.x OEM key from PC firmware
#ACPI -> table MSDM -> raw content -> byte offset 56 to end
#ck, 03-Jan-2014 (christian@korneck.de)
#####################################################


def GetWindowsKey():
	#returns Windows Key as string
	table=b"MSDM"
	if acpi.FindAcpiTable(table)==True:
		try:
			rawtable = acpi.GetAcpiTable(table)
			#http://msdn.microsoft.com/library/windows/hardware/hh673514
			#byte offset 36 from beginning = Microsoft 'software licensing data structure' / 36 + 20 bytes offset from beginning = Win Key
			return rawtable[56:len(rawtable)].decode("utf-8")
		except:
			return False
	else:
		print("[ERR] - ACPI table " + str(table) + " not found on this system")
		return False

try:
	WindowsKey=GetWindowsKey()
	if WindowsKey==False:
		print("unexpected error")
		sys.exit(1)
	else:
		print(str(WindowsKey))
except:
	print("unexpected error")
	sys.exit(1)
