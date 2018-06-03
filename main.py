
import argparse
from Objects.Worker import Worker


def main():
    mover = Worker()
    ret = mover.treat_file(args.file_path)
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='File with indications')
    args = parser.parse_args()
    main()
