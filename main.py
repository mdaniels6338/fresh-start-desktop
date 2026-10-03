"""Fresh Start Desktop — A local helper for Fresh Start cleaning-job folders, house files, and tidy photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='fresh_start_desktop',
        description='A local helper for Fresh Start cleaning-job folders, house files, and tidy photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Fresh Start Desktop')
    print('Keep the job list on disk before a new house.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
