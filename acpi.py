import ctypes
import ctypes.wintypes

def EnumAcpiTables():
#returns a list of the names of the ACPI tables on this system
	FirmwareTableProviderSignature=ctypes.wintypes.DWORD(1094930505)
	pFirmwareTableBuffer=ctypes.create_string_buffer(0)
	BufferSize=ctypes.wintypes.DWORD(0)
	#http://msdn.microsoft.com/en-us/library/windows/desktop/ms724259
	EnumSystemFirmwareTables=ctypes.WinDLL("Kernel32").EnumSystemFirmwareTables
	ret=EnumSystemFirmwareTables(FirmwareTableProviderSignature, pFirmwareTableBuffer, BufferSize)
	pFirmwareTableBuffer=None
	pFirmwareTableBuffer=ctypes.create_string_buffer(ret)
	BufferSize.value=ret
	ret2=EnumSystemFirmwareTables(FirmwareTableProviderSignature, pFirmwareTableBuffer, BufferSize)
	return [pFirmwareTableBuffer.value[i:i+4] for i in range(0, len(pFirmwareTableBuffer.value), 4)]

def FindAcpiTable(table):
#checks if specific ACPI table exists and returns True/False
	tables = EnumAcpiTables()
	if table in tables:
		return True
	else:
		return False

def GetAcpiTable(table):
#returns raw contents of ACPI table
	#http://msdn.microsoft.com/en-us/library/windows/desktop/ms724379x
	tableID = 0
	for b in reversed(table):
		tableID = (tableID << 8) + b
	GetSystemFirmwareTable=ctypes.WinDLL("Kernel32").GetSystemFirmwareTable
	FirmwareTableProviderSignature=ctypes.wintypes.DWORD(1094930505)
	FirmwareTableID=ctypes.wintypes.DWORD(int(tableID))
	pFirmwareTableBuffer=ctypes.create_string_buffer(0)
	BufferSize=ctypes.wintypes.DWORD(0)
	ret = GetSystemFirmwareTable(FirmwareTableProviderSignature, FirmwareTableID, pFirmwareTableBuffer, BufferSize)
	pFirmwareTableBuffer=None
	pFirmwareTableBuffer=ctypes.create_string_buffer(ret)
	BufferSize.value=ret
	ret2 = GetSystemFirmwareTable(FirmwareTableProviderSignature, FirmwareTableID, pFirmwareTableBuffer, BufferSize)
	return pFirmwareTableBuffer.raw
