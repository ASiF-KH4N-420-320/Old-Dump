import os, platform
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            import sifvvx
        elif bit == '32bit':
            import asif32
Run()
