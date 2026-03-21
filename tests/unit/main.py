import os
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='infra-terraform CLI')
    parser.add_argument('-t', '--target', type=str, help='target environment', required=True)
    parser.add_argument('-a', '--action', type=str, help='action to perform', required=True)
    args = parser.parse_args()

    if args.action not in ['apply', 'destroy']:
        parser.error(f'Invalid action: {args.action}')

    if args.target not in ['dev', 'prod']:
        parser.error(f'Invalid target: {args.target}')

    current_dir = Path.cwd()
    terraform_dir = current_dir / 'terraform'
    if not terraform_dir.exists():
        print(f'Error: terraform directory not found at {terraform_dir}')
        sys.exit(1)

    env_dir = terraform_dir / args.target
    if not env_dir.exists():
        print(f'Error: environment directory not found at {env_dir}')
        sys.exit(1)

    os.chdir(env_dir)
    os.system(f'terraform {"apply" if args.action == "apply" else "destroy"}')

if __name__ == '__main__':
    main()