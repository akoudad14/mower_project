
import argparse
from Objects.Worker import Worker


def main():
    mover = Worker()
    try:
        with open(args.file_path, "r", encoding='utf-8') as fp:
            lines = fp.read().splitlines()
    except UnicodeEncodeError:
        print('Encoding file problem')
        ret = -1
    else:
        ret = mover.work(lines)
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='File with indications')
    args = parser.parse_args()
    main()
