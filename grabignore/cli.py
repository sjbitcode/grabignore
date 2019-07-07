import argparse

from grabignore import fetch


def parse_args():
    parser = argparse.ArgumentParser(description='Grab your favorite .gitignore')
    parser.add_argument('language', nargs='+', type=str,
                        help='Language name of gitignore file')
    parser.add_argument('--dest', '-d', type=str, default='.',
                        help='File destination')
    parser.add_argument('--reload', '-r', action='store_true', default=False,
                        help='Reload list of supported gitignore files')
    return parser.parse_args()


def safe_entrypoint():
    try:
        # Parse args
        args = parse_args()
        languages = args.language
        ignore_output_name = True if len(languages) > 1 else False
        dest = args.dest

        # Initialize gitignore fetcher
        g = fetch.GitignoreFetch()

        # Pull fresh list of gitignores if specified by user
        if args.reload:
            g.update()

        # Download gitignores
        for language in languages:
            g.download(language, destination=dest,
                       ignore_output_name=ignore_output_name)

    except Exception as e:
        print(e.__str__())
