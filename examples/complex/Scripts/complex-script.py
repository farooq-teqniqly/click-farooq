#!c:\src\my\click\examples\complex\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'click-example-complex','console_scripts','complex'
__requires__ = 'click-example-complex'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('click-example-complex', 'console_scripts', 'complex')()
    )
