import os
import subprocess
import sys

if __name__ == '__main__':
    date = sys.argv[1]
    msg = sys.argv[2]

    k = os.environ.copy()
    k['GIT_AUTHOR_DATE'] = date
    k['GIT_COMMITTER_DATE'] = date

    subprocess.run(['git', 'commit', '-m', msg], env=k)

