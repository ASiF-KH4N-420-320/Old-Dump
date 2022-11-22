import os, platform
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            import sif64md
        elif bit == '32bit':
            import asif32
Run()
