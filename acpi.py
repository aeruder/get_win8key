import sys

if sys.platform.startswith('win32'):
    pass
elif sys.platform.startswith('linux'):
    pass
else:
    raise NotImplementedError('acpi support only implemented for linux and win32')
